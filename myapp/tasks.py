from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json
# from django.contrib.auth import get_user_model
from celery import shared_task
# from django.core.mail import send_mail
# from food_delivery import settings

@shared_task
def send_order_notification(user_id, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'user_{user_id}',
        {
            'type': 'send.notification',
            'message': message,
            'notification_type': 'order',
        }
    )

@shared_task
def send_payment_notification(user_id, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'user_{user_id}',
        {
            'type': 'send.notification',
            'message': message,
            'notification_type': 'payment',
        }
    )

