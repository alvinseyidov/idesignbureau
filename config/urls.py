from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home import views as home_views
from shop import views as shop_views
from fotooboy import views as fotooboy_views
from skinali import views as skinali_views
from carpet import views as carpet_views
from furniture import views as furniture_views
from evdekor import views as evdekor_views
from product import views as product_views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', home_views.index, name="index"),
    path('', home_views.index, name="filials"),

    path('cat/fotooboy/', home_views.fotooboy, name="fotooboy"),
    path('cat/fotooboy/gallery/', fotooboy_views.fotooboygallery, name="fotooboygallery"),
    path('cat/fotooboy/material/', fotooboy_views.fotooboymaterial, name="fotooboymaterial"),
    path('cat/fotooboy/ready/', fotooboy_views.fotooboyready, name="fotooboyready"),
    path('cat/fotooboy/glue/', fotooboy_views.fotooboyglue, name="fotooboyglue"),
    path('cat/fotooboy/portfolio/', fotooboy_views.fotooboyportfolio, name="fotooboyportfolio"),
    path('cat/fotooboy/customers/', fotooboy_views.fotooboycustomers, name="fotooboycustomers"),
 
 

    path('cat/carpets/', carpet_views.products, name="carpets"),
    path('cat/carpets/<int:id>/', carpet_views.product, name="carpet"),

    path('cat/furnitures/', furniture_views.products, name="furnitures"),
    path('cat/furnitures/<int:id>/', furniture_views.product, name="furniture"),

 
    path('cat/skinali/', home_views.skinali, name="skinali"),
    path('cat/skinali/portfolio/', skinali_views.portfolio, name="skinaliportfolio"),

    path('cat/evdekor/', home_views.evdekor, name="evdekor"),
    path('cat/evdekor/portfolio/', evdekor_views.portfolio, name="evdekorportfolio"),

    path('contact/', home_views.contact, name="contact"),
    path('about/', home_views.about, name="about"),
    path('cart/', shop_views.cart, name="cart"),
    path('clearcart/', shop_views.clearcart, name="clearcart"),
    path('search/', home_views.search, name="search"),
    path('filter/<int:id>/', home_views.filter, name="filter"),
    path('otaq/<int:id>/', home_views.filterotaq, name="filterotaq"),
    path('reng/<int:id>/', home_views.filterreng, name="filterreng"),
    path('', home_views.index, name="shipping"),
    path('category/<int:id>/', product_views.main_category, name="category"),
    path('product/<int:id>/', product_views.product, name="product"),
    path('producttablo/<int:id>/', product_views.producttablo, name="producttablo"),


    path('ordernow/', shop_views.order_now, name="order_now"),
    path('successpay/', shop_views.success, name="successpay"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

