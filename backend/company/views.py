from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Customer, Quote, Inventory, Insurance, Schedule

def calculate_cost(items, distance):
    base_rate = 500
    per_km_rate = 15
    per_item_rate = 50
    return base_rate + (per_km_rate * distance) + (per_item_rate * items)


def is_admin(user):
    return user.is_authenticated and user.is_staff


def home(request):
    quotes = Quote.objects.all().select_related('customer')
    total_quotes = quotes.count()
    pending_quotes = quotes.filter(status='Pending').count()
    completed_quotes = quotes.filter(status='Completed').count()
    
    context = {
        'quotes': quotes[:10],
        'total_quotes': total_quotes,
        'pending_quotes': pending_quotes,
        'completed_quotes': completed_quotes,
    }
    return render(request, 'home.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                is_staff=False
            )
            messages.success(request, f'Account created successfully! Welcome, {username}!')
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
            return redirect('home')
    
    return render(request, 'signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:
                messages.success(request, f'Welcome back, Admin {user.username}!')
            else:
                messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
    return redirect('home')


@login_required
def quote_form(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        move_date = request.POST.get('move_date')
        items = int(request.POST.get('items', 0))
        distance_km = float(request.POST.get('distance_km', 0))
        
        estimated_cost = calculate_cost(items, distance_km)
        
        customer, created = Customer.objects.get_or_create(
            email=email,
            defaults={
                'name': customer_name,
                'phone': phone,
                'address': address,
            }
        )
        
        if not created:
            customer.name = customer_name
            customer.phone = phone
            customer.address = address
            customer.save()
        
        quote = Quote.objects.create(
            customer=customer,
            move_date=move_date,
            items=items,
            distance_km=distance_km,
            estimated_cost=estimated_cost,
        )
        
        messages.success(request, f'Quote created successfully! Estimated cost: ₹{estimated_cost:.2f}')
        return redirect('quote_detail', quote_id=quote.id)
    
    return render(request, 'quote_form.html')


@login_required
def quote_detail(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    inventory_items = quote.inventory_items.all()
    schedules = quote.schedules.all()
    insurance_claims = quote.insurance_claims.all()
    
    context = {
        'quote': quote,
        'inventory_items': inventory_items,
        'schedules': schedules,
        'insurance_claims': insurance_claims,
    }
    return render(request, 'quote_detail.html', context)


@login_required
def inventory(request, quote_id=None):
    if request.method == 'POST' and quote_id:
        quote = get_object_or_404(Quote, id=quote_id)
        item_name = request.POST.get('item_name')
        quantity = int(request.POST.get('quantity', 1))
        fragile = request.POST.get('fragile') == 'on'
        
        Inventory.objects.create(
            quote=quote,
            item_name=item_name,
            quantity=quantity,
            fragile=fragile,
        )
        
        messages.success(request, f'Item "{item_name}" added to inventory.')
        return redirect('inventory_detail', quote_id=quote_id)
    
    if quote_id:
        quote = get_object_or_404(Quote, id=quote_id)
        inventory_items = quote.inventory_items.all()
        context = {
            'quote': quote,
            'inventory_items': inventory_items,
        }
        return render(request, 'inventory.html', context)
    
    quotes = Quote.objects.all().select_related('customer')
    context = {'quotes': quotes}
    return render(request, 'inventory.html', context)


@user_passes_test(is_admin)
def schedule(request):
    if request.method == 'POST':
        quote_id = request.POST.get('quote_id')
        quote = get_object_or_404(Quote, id=quote_id)
        scheduled_date = request.POST.get('scheduled_date')
        scheduled_time = request.POST.get('scheduled_time')
        driver_name = request.POST.get('driver_name', '')
        vehicle_number = request.POST.get('vehicle_number', '')
        notes = request.POST.get('notes', '')
        
        schedule_obj = Schedule.objects.create(
            quote=quote,
            scheduled_date=scheduled_date,
            scheduled_time=scheduled_time,
            driver_name=driver_name,
            vehicle_number=vehicle_number,
            notes=notes,
        )
        
        messages.success(request, f'Move scheduled for {scheduled_date} at {scheduled_time}')
        return redirect('schedule')
    
    schedules = Schedule.objects.all().select_related('quote__customer').order_by('scheduled_date', 'scheduled_time')
    quotes = Quote.objects.filter(status__in=['Pending', 'Approved'])
    
    context = {
        'schedules': schedules,
        'quotes': quotes,
    }
    return render(request, 'schedule.html', context)


@login_required
def insurance(request):
    if request.method == 'POST':
        quote_id = request.POST.get('quote_id')
        quote = get_object_or_404(Quote, id=quote_id)
        
        if request.user.is_staff:
            claim_status = request.POST.get('claim_status', 'Pending')
        else:
            claim_status = 'Pending'
        
        claim_amount = request.POST.get('claim_amount')
        claim_description = request.POST.get('claim_description', '')
        
        claim_amount = float(claim_amount) if claim_amount else None
        
        insurance_obj = Insurance.objects.create(
            quote=quote,
            claim_status=claim_status,
            claim_amount=claim_amount,
            claim_description=claim_description,
        )
        
        if request.user.is_staff:
            messages.success(request, f'Insurance claim created with status: {claim_status}')
        else:
            messages.success(request, 'Insurance claim submitted successfully! It will be reviewed by admin.')
        return redirect('insurance')
    
    claims = Insurance.objects.all().select_related('quote__customer').order_by('-created_at')
    quotes = Quote.objects.all()
    
    context = {
        'claims': claims,
        'quotes': quotes,
    }
    return render(request, 'insurance.html', context)


@user_passes_test(is_admin)
def update_quote_status(request, quote_id):
    if request.method == 'POST':
        quote = get_object_or_404(Quote, id=quote_id)
        new_status = request.POST.get('status')
        quote.status = new_status
        quote.save()
        messages.success(request, f'Quote status updated to {new_status}')
    return redirect('quote_detail', quote_id=quote_id)


@user_passes_test(is_admin)
def update_claim_status(request, claim_id):
    if request.method == 'POST':
        claim = get_object_or_404(Insurance, id=claim_id)
        new_status = request.POST.get('status')
        claim_amount = request.POST.get('claim_amount')
        
        claim.claim_status = new_status
        if claim_amount:
            claim.claim_amount = float(claim_amount)
        claim.save()
        
        messages.success(request, f'Insurance claim status updated to {new_status}')
    return redirect('insurance')
