from django.shortcuts import render
from .models import Product
from product.models import SubCategory, Color, Category, Room, Interier
from shop.models import Customer, OrderItem, Order
from home.models import *
from django.db.models import Q

def products(request):
    featured = SubCategory.objects.filter(parent__isnull=True) 
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.all()
    colors = Color.objects.all()
    context = {
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
    }
    return render(request, "cats/furnitures.html", context)



def product(request, id):
    product = Product.objects.get(pk=id)
    categories = Category.objects.all()
    cat_id = id

    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.all()[:10]
    colors = Color.objects.all()
    rooms = Room.objects.all()
    interiers = Interier.objects.all()

 



    context = {
        'product': product,
        'categories': categories,
        'cat_id': cat_id,
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
        'rooms': rooms,
        'interiers': interiers
    }

    return render(request, "cats/furniture.html", context)