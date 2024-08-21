from django import forms
from .models import User_name, Order_name, Payment_status


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User_name
        fields = ['name', 'mail', 'password']


class OrderForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(queryset=User_name.objects.all(), empty_label=None, to_field_name='name', label='User')
    class Meta:
        model = Order_name
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment_status
        fields = '__all__'

        


