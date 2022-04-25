from django.shortcuts import render, redirect
from product.models import *
from shop.models import Customer, OrderItem, Order
from .forms import ContactForm
from .models import *
from django.db.models import Q
 

def index(request):

    featured = SubCategory.objects.filter(parent__isnull=True) 
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.filter(is_featured=True)
    colors = Color.objects.all()
    rooms = Room.objects.all()
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
        'rooms': rooms,
    }
    if request.method == 'POST':
        product = Product.objects.get(id=request.POST.get('pr'))
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity = request.POST['quantity']
        orderItem.save()
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        context = {'order': order}

        return render(request, 'cart.html', context)
            
    return render(request, "index.html", context)

def fotooboy(request):
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.all()[:10]
    colors = Color.objects.all()
    rooms = Room.objects.all()
    context = {
        
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
        'rooms': rooms,
    }
    return render(request, "cats/fotooboy.html", context)

def tablo(request):
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.all()[:10]
    colors = Color.objects.all()
    rooms = Room.objects.all()
    context = {
        
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
        'rooms': rooms,
    }
    return render(request, "cats/tablo.html", context)

def selftablo(request):
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.all()[:10]
    colors = Color.objects.all()
    rooms = Room.objects.all()
    context = {
        
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
        'rooms': rooms,
    }
    return render(request, "cats/selftablo.html", context)

def skinali(request):
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.filter(main_category=4)
    colors = Color.objects.all()
    rooms = Room.objects.all()
    context = {
        
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
        'rooms': rooms,
    }
    return render(request, "cats/skinali.html", context)

def evdekor(request):
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.all()[:10]
    colors = Color.objects.all()
    rooms = Room.objects.all()
    context = {
        
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
        'rooms': rooms,
    }
    return render(request, "cats/evdekor.html", context)
    
def exclusive(request):
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.all()[:10]
    colors = Color.objects.all()
    rooms = Room.objects.all()
    context = {
        
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
        'rooms': rooms,
    }
    return render(request, "cats/exclusive.html", context)

    
def search(request):
    query = request.GET.get("q")
    products = Product.objects.filter( Q(name__icontains=query) )
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    if request.method == 'POST':
        product = Product.objects.get(id=request.POST.get('pr'))
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity = request.POST['quantity']
        orderItem.save()
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        context = {'order': order}

        return render(request, 'cart.html',context)
    context = {
        
        'products': products,
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,

    }
    return render(request, "search.html", context)

def filter(request,id): 
    query = SubCategory.objects.get(pk=id)
    products = Product.objects.filter(sub_category__pk=id)
    
    featured = SubCategory.objects.filter(parent__isnull=True) 
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()

    if request.method == 'POST':
        product = Product.objects.get(id=request.POST.get('pr'))
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity = request.POST['quantity']
        orderItem.save()
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        context = {'order': order}

        return render(request, 'cart.html',context)

    context = {
        
        'products': products,
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'query': query,

    }
    return render(request, "filter.html", context)

def cart(request):
	try:
		customer = request.user.customer
	except:
		device = request.COOKIES['device']
		customer, created = Customer.objects.get_or_create(device=device)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	context = {'order':order}
	return render(request, 'cart.html', context)


def filterotaq(request,id):
    query = Room.objects.get(pk=id)
    products = Product.objects.filter(room__pk=id)
    
    featured = SubCategory.objects.filter(parent__isnull=True) 
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()

    context = {
        
        'products': products,
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'query': query,

    }
    return render(request, "filterotaq.html", context)

def filterreng(request,id):
    query = Color.objects.get(pk=id)
    products = Product.objects.filter(color__pk=id)
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()

    context = {
        
        'products': products,
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'query': query,

    }
    return render(request, "filterreng.html", context)

def about(request):
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()

    context = {
        
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,

    }
    return render(request, "about.html", context)

"""
def index(request):
    
    featured = SubCategory.objects.filter()
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    products = Product.objects.filter(is_featured=True)
    colors = Color.objects.all()
    rooms = Room.objects.all()
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'featured': featured,
        'general': general,
        'clients': clients,
        'socials': socials,
        'products': products,
        'colors': colors,
        'rooms': rooms,
    }
    if request.method == "POST":
        images = request.FILES.getlist('images')
        print("hey hey---------------------------------------------------------------------------------------------------------------1")
        n = 15
        name = "3D АРКИ "
        for image in images:
            print("hey hey------------------------------------------------------------------------------------------------------------")
            n = n + 1
            nm = name + str(n)
            category = Category.objects.get(pk=1)
            product = Product.objects.create(main_category=category,price=150,name=nm)
            image = ProductImage.objects.create(image = image, product=product)
    return render(request, "index.html", context)
"""


def contact(request):
    
    general = General.objects.all()[0]
    clients = Client.objects.all()
    socials = Social.objects.all()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                
                'general': general,
                'clients': clients,
                'socials': socials,
            }
            return render(request, "success.html", context)

    context = {
        
        'general': general,
        'clients': clients,
        'socials': socials,
    }
    return render(request, 'contact.html', context)
