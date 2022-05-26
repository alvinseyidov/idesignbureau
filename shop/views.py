from django.shortcuts import render, redirect
from .models import *
from kapital_gateway import KapitalPayment

def cart(request):
	device = request.COOKIES['device']
	customer, created = Customer.objects.get_or_create(device=device)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	context = {'order':order}
	return render(request, 'cart.html', context)


def clearcart(request):
	device = request.COOKIES['device']
	customer, created = Customer.objects.get_or_create(device=device)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	order.delete()
	context = {'order':order}
	return render(request, 'cart.html', context)

def order_now(request):
	gateway = KapitalPayment(merchant_id="E1000010",approve_url="http://127.0.0.1:8000/successpay",cancel_url="https://test.com/cancel", decline_url="https://test.com/decline", )
	result = gateway.create_order(amount=10000, currency=944, description="Idesignbureau.com", lang="AZ")
	print(result)
	return redirect(result['url'])

def success(request):
	gateway = KapitalPayment(merchant_id="E1000010",approve_url="https://test.com/approve",cancel_url="https://test.com/cancel", decline_url="https://test.com/decline", )
	result = gateway.create_order(amount=10, currency=944, description="Idesign ", lang="AZ")
	print(result)
	return render(request, 'successpay.html')