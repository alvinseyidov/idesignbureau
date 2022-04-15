from django.shortcuts import render
from product.models import *
from home.models import *

def portfolio(request):
    products = Product.objects.all()
    categories = Category.objects.all() 
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
        'sub_categories': sub_categories,
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'colors': colors,
        'rooms': rooms,
    }

    return render(request, 'cats/evdekor/portfolio.html', context)