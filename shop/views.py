from django.shortcuts import render
from .models import *


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