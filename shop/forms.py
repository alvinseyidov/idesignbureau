from django import forms
from .models import FastOrder




class OrderForm(forms.ModelForm):
    class Meta:
        model = FastOrder
        fields = '__all__'
