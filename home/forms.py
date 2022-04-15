from django import forms
from .models import Contact, Order


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
