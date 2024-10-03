from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Bus(models.Model):
    bus_name=models.CharField(max_length=100)
    seat_available=models.IntegerField(default=0)
    seat_remaining=models.IntegerField(default=0,null=True)
    source=models.CharField(max_length=200,default='')
    destination = models.CharField(max_length=200, null=True)
    bus_fare=models.IntegerField()
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    arrival=models.DateTimeField(null=True)
    cancellation_policy = models.TextField(blank=True, null=True)
    refund_policy = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.bus_name

   
    
class Tickets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='tickets')
    name = models.CharField(max_length=200)
    fare = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    seats = models.IntegerField()
    ticket_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.name} on {self.bus.bus_name}"
    def total_fare(self):
        return self.fare * self.seats
    


    # payment_method = models.CharField(max_length=50, choices=[
    #     ('G-Pay', 'G-Pay'),
    #     ('PhonePe', 'PhonePe'),
    #     ('Paytm', 'Paytm')
    # ], blank=True, null=True)  # Payment method
    # payment_status = models.CharField(max_length=20, default='Pending', choices=[
    #     ('Pending', 'Pending'),
    #     ('Paid', 'Paid'),
    #     ('Failed', 'Failed')
    # ])  # Payment status

    def __str__(self):
        return f"Ticket for {self.name} on {self.bus.bus_name}"
    



class TicketBooking(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_tickets = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        bus = self.bus
        bus.seat_remaining -= self.num_tickets
        bus.save()
        super().save(*args, **kwargs)
