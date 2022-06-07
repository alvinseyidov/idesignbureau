from django.shortcuts import render, redirect

from home.forms import ContactForm
from shop.forms import OrderForm
from shop.models import Customer, OrderItem, Order
from .models import *
from home.models import *
from fotooboy.models import *
 

def main_category(request, id):
    products = Product.objects.filter(main_category__pk=id)
    categories = Category.objects.all()
    cat_id = id
    sub_categories = SubCategory.objects.all()

    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    colors = Color.objects.all()
    rooms = Room.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'cat_id': cat_id,
        'sub_categories': sub_categories,
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'colors': colors,
        'rooms': rooms,
    }

    return render(request, "main_category.html", context)


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

    material = Material.objects.all()

    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
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
                'interiers': interiers,
            }
            return render(request, "ordersuccess.html", context)



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
        'material': material,
        'interiers': interiers
    }

    return render(request, "product.html", context)

def producttablo(request, id):
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

    material = Material.objects.all()

    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
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
                'interiers': interiers,
            }
            return render(request, "ordersuccess.html", context)



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
        'material': material,
        'interiers': interiers
    }

    return render(request, "producttablo.html", context)

