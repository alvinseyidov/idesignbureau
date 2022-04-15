from django.shortcuts import render
from product.models import *
from .forms import ContactForm
from .models import *
from django.db.models import Q
 

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
        n = 0
        name = request.POST['name']
        for image in images:
            print("hey hey------------------------------------------------------------------------------------------------------------")
            n = n + 1
            nm = name + " " + str(n)
            sub = SubCategory.objects.get(pk=5)
            category = Category.objects.get(pk=1)
            product = Product.objects.create(main_category=category,price=30,sub_category=sub,name=nm)
            image = ProductImage.objects.create(image = image, product=product)
            #list = request.POST['tags'].split()
            #for l in list:
                #tag = Tag.objects.filter(name=l).last()
                #if tag:
                    #product.tags.add(tag)
            list = ['nature', 'way', 'road', 'searoad', 'seaway', 'yol', 'menzere', 'tebiet', 'pirs', 'deniz', '3d', '3д', 'gold', 'golden', 'flower', 'jewelry', 'цветы', 'бижутерия', 'золото', 'золотые', 'qizil', 'altin', 'gul', 'guller', '3d gul', '3d guller', 'flowers', 'hall', 'koridor', 'xol', 'стереоскопические', 'стерео', 'расширяющие', 'пространство', 'stereoscopic', 'qenishlendirici', 'geometry', 'geometrik', 'геометрия', 'мост', 'bridge', 'most', 'korpu', 'sheher', 'city', 'cityview', 'город', 'потолок', 'tavan', 'asma tavan', 'ceiling', 'wall', 'leaf', 'стена', 'листья', 'yashilliq', 'street', 'old town', 'old street', 'kuche', 'kohne sheher', 'улица', 'улочка', 'старый город', 'природа', 'фреска', 'fresco', 'freska', 'лепка', 'divar', 'lepka', 'фальшстена', 'геометрические', 'вид фреска', 'view', 'barelief', 'relief', 'relief flower', 'barelyef', 'relyef', 'барельеф', 'рельеф', 'tree', 'trees', 'дерево', 'деревья', 'agac', 'agaclar', 'grafity', 'grafiti', 'графити', 'графика', 'рисунок', 'resim', 'grafik', 'woman', 'women', 'girl', 'девушка', 'девушки', 'девочка', 'женщина', 'красота', 'xanim', 'qadin', 'qadinlar', 'gozellik', 'gozel', 'disney', 'disneyland', 'дисней', 'динейленд', 'диснэйлэнд', 'детские', 'улицы', 'disneylend', 'usaq', 'ushaq oboy', 'cizgi film', 'marvel', 'dc', 'iron man', 'spiderman', 'spider', 'человек паук', 'марвел', 'кино', 'герои', 'детские обои', 'kids wall', 'kids', 'kids wallpaper', 'ballet', 'balet', 'балет', 'балерина', 'ushaq otaq', 'kids background', 'горы', 'вектор', 'ushag', 'animals', 'heyvan', 'heyvanlar', 'kids animal', 'baloon', 'balloon', 'шар', 'воздушный шар', 'шары', 'shar', 'sharik', 'животные', 'plane', 'samolet', 'самолет', 'teyyare', 'world map', 'dunya xerite', 'xerite', 'map', 'карта', 'карта мира', 'kosmos', 'space', 'космос', 'авто', 'мото', 'машина', 'машинки', 'поезд', 'транспорт', 'mashin', 'avto', 'auto', 'moto', 'motocikl', 'motocycle', 'bike', 'mcqueen', 'pirat', 'pirate', 'sea', 'пират', 'princess', 'prenses', 'princes', 'принцесса', 'принцессы', 'замок', 'спорт', 'футбол', 'хоккей', 'баскетбол', 'теннис', 'futbol', 'football', 'soccer', 'sport', 'gym', 'fitness', 'animal', 'тигр', 'лев', 'леопард', 'слон', 'павлин', 'олень', 'maral', 'peacock', 'pavlin', 'tovuz qush', 'peleng', 'shir', 'leopard', 'аквариум', 'akvarium', 'aqua', 'рыбки', 'подводный мир', 'sualti', 'крылья', 'wing', 'wings', 'lips', 'мрамор', 'абстракт', 'текстура', 'mermer', 'abstrakt', 'abstract', 'marble', 'tekstur', 'texture', 'onyx', 'oniks', 'music', 'musiqi', 'музыка', 'мужчина', 'пара', 'любовь', 'романтика', 'kishi', 'sevgi', 'romantik', 'cutluk', 'cut', 'man', 'men', 'couple', 'love', 'romance', 'romantic', 'forest', 'лес', 'gorunush', 'shelale', 'waterfall', 'пейзаж', 'islam', 'mekka', 'allah', 'религия', 'буддизм', 'buddah', 'budda', 'ислам', 'бог', 'салон', 'saloon', 'salon', 'beauty', 'azerbaijan', 'baku', 'azerbaycan', 'баку', 'азербайджан', 'cities', 'страна', 'sheherler', 'olkeler', 'amerika', 'usa', 'америка', 'ingiltere', 'britain', 'uk', 'англия', 'misir', 'egypt', 'египет', 'italy', 'italiya', 'италия', 'rawn city', 'resimli sheher', 'france', 'fransa', 'франция', 'кофе', 'kofe', 'yemek', 'frukt', 'vintage', 'vintaj', 'винтаж', 'орхидеи', 'orchid', 'orxideya', 'lelek', 'lelekler', 'перья', 'перо', 'feather', 'rose', 'роза', 'розы', 'gizilgul', 'qizilgul', 'qush', 'qushlar', 'птицы', 'birds']
            for l in list:
                Tag.objects.create(name=l)
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
    return render(request, "filter.html", context)

def filterotaq(request,id):
    query = Room.objects.get(pk=id)
    products = Product.objects.filter(room__pk=id)
    
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
