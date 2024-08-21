from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class User_name(models.Model):
    user_id = models.AutoField(editable=False, primary_key=True)
    name = models.CharField(max_length=20, default='Your name')
    mail = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Order_name(models.Model):
    user_id = models.ForeignKey(User_name, on_delete=models.CASCADE) 
    order_id = models.AutoField(editable=False, primary_key=True)
    order_date = models.DateField(auto_now_add=True)
    order_item = models.CharField(max_length=100, default='ice-cream')
    restaurant_name = models.CharField(max_length=50, default='Fort')


class Payment_status(models.Model):
    payment_id = models.AutoField(editable=False, primary_key=True) 
    user_id = models.ForeignKey(User_name, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order_name, on_delete=models.CASCADE)
    PAYMENT_STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('processing', 'Processing'),
        ('declined', 'Declined'),
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='processing')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment Status for Order {self.order_id}"
    


class Notification_status(models.Model):
    user_id = models.ForeignKey(User_name, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order_name, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    payment_id = models.ForeignKey(Payment_status, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notification for Order {self.order_id}"