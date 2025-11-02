from django.contrib import admin
from .models import Customer, Quote, Inventory, Insurance, Schedule

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_at']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['created_at']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['customer', 'move_date', 'items', 'distance_km', 'estimated_cost', 'status', 'created_at']
    list_filter = ['status', 'move_date', 'created_at']
    search_fields = ['customer__name', 'customer__email']
    readonly_fields = ['estimated_cost', 'created_at']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['quote', 'item_name', 'quantity', 'fragile']
    list_filter = ['fragile']
    search_fields = ['item_name', 'quote__customer__name']

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['quote', 'claim_status', 'claim_amount', 'created_at']
    list_filter = ['claim_status', 'created_at']
    search_fields = ['quote__customer__name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['quote', 'scheduled_date', 'scheduled_time', 'driver_name', 'status']
    list_filter = ['status', 'scheduled_date']
    search_fields = ['quote__customer__name', 'driver_name', 'vehicle_number']
