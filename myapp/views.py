from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .forms import OrderForm, PaymentForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Order_name



def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save()
            payment = payment_form.save(commit=False)
            payment.order = order
            payment.save()
            return redirect('order-list')
    else:
        order_form = OrderForm()
        payment_form = PaymentForm()
    return render(request, 'myapp/create_order.html', {'order_form': order_form, 'payment_form': payment_form})


def orders_view(request):
    orders = Order_name.objects.all()
    return render(request, 'myapp/orders.html', {'orders': orders})


def update_order_status(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order_name, id=order_id)
        new_status = request.POST.get("status")

        order.status = new_status
        order.save()

        return JsonResponse({"message": "Status updated successfully."})
    else:
        return JsonResponse({"error": "Invalid request method."})
    


class IndexViewSet(APIView):
    def get(self, request):
        return render(request, "myapp/index.html")
    

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, OrderForm, PaymentForm
from .models import User_name, Order_name, Payment_status, Notification_status



def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']

            
            user = User_name.objects.create(name=name, mail=mail, password=password)
            user.save()

            return redirect('place-order')
    else:
        form = UserRegistrationForm()

    return render(request, 'myapp/register_user.html', {'form': form})


def user_list(request):
    users = User_name.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})


def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            restaurant_name = form.cleaned_data['restaurant_name']
            order = Order_name(user_id=user_id,restaurant_name=restaurant_name)
            order.save()
            
            return redirect('make-payment')  
        else:
            return redirect('user-login')
    else:
        form = OrderForm()
    
    return render(request, 'myapp/create_order.html',{'form': form})


def orders_view(request):
    orders = Order_name.objects.all()
    return render(request, 'myapp/orders.html', {'orders': orders})



def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id'] 
            payment_status = form.cleaned_data['payment_status']
            payment_amount = form.cleaned_data['payment_amount']
            order_id = form.cleaned_data['order_id'] 
            payment_details = Payment_status(user_id=user_id,payment_status=payment_status, payment_amount=payment_amount,order_id=order_id)
            payment_details.save()

            Notification_status.objects.create(
                user_id=user_id,
                order_id=order_id,
                message="Payment has been made.",
                payment_id = payment_details

            )

            return redirect('http://localhost:8000/send-email/')

        
    else:
        form = PaymentForm()

    return render(request, 'myapp/make_payment.html', {'form': form})


def payment_list(request):
    payments = Payment_status.objects.all()
    return render(request, 'myapp/payment_list.html', {'payments': payments})


# @login_required
def notification_list(request):
    notifications = Notification_status.objects.all()
    return render(request, 'myapp/notification_list.html', {'notifications': notifications})



from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import redirect, render

def send_email(request):
    if request.method=="POST":
        email_id = request.POST.get('email_id')
        response_data = "email send to "+email_id
        email_name = email_id.split('@')

        email_template = render_to_string(
            'myapp/email.html', {"username": email_name[0]})
        email_obj = EmailMultiAlternatives(
            "Email Notification Example",
            "Email Notification Example",
            settings.EMAIL_HOST_USER,
            [email_id],
        )
        email_obj.attach_alternative(email_template, 'text/html')
        email_obj.send()
        context = {"data":response_data}
        return render(request, 'myapp/index.html', context)
    else:
        context = {"data":"response_data"}
        return render(request,"myapp/index1.html")

