from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Quote(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='quotes')
    move_date = models.DateField()
    items = models.IntegerField()
    distance_km = models.FloatField()
    estimated_cost = models.FloatField()
    status = models.CharField(max_length=20, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Quote for {self.customer.name} - ₹{self.estimated_cost}"
    
    class Meta:
        ordering = ['-created_at']


class Inventory(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='inventory_items')
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    fragile = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.item_name} (x{self.quantity})"
    
    class Meta:
        verbose_name_plural = "Inventory items"


class Insurance(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='insurance_claims')
    claim_status = models.CharField(max_length=50, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Settled', 'Settled'),
    ])
    claim_amount = models.FloatField(null=True, blank=True)
    claim_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Insurance Claim - {self.quote.customer.name} - {self.claim_status}"
    
    class Meta:
        ordering = ['-created_at']


class Schedule(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='schedules')
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()
    driver_name = models.CharField(max_length=100, blank=True)
    vehicle_number = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='Scheduled', choices=[
        ('Scheduled', 'Scheduled'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Schedule - {self.quote.customer.name} on {self.scheduled_date}"
    
    class Meta:
        ordering = ['scheduled_date', 'scheduled_time']
