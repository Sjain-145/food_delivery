from django.contrib import admin
from .models import User_name, Order_name, Payment_status, Notification_status

class UsernameAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'mail', 'password')  

class PaymentStatusAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'user_id', 'get_order_id', 'payment_amount', 'payment_status')

    def get_order_id(self, obj):
        return obj.order_id.order_id  
    get_order_id.short_description = 'Order ID'

admin.site.register(User_name, UsernameAdmin)  
admin.site.register(Order_name)
admin.site.register(Payment_status, PaymentStatusAdmin)  
admin.site.register(Notification_status)  
