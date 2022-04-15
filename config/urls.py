from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home import views as home_views
from fotooboy import views as fotooboy_views
from skinali import views as skinali_views
from tablo import views as tablo_views
from selftablo import views as selftablo_views
from exclusive import views as exclusive_views
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

    path('cat/tablo/', home_views.tablo, name="tablo"),
    path('cat/tablo/ketan/', tablo_views.ketan, name="tabloketan"),
    path('cat/tablo/modular/', tablo_views.modular, name="tablomodular"),
    path('cat/tablo/calculator/', tablo_views.calculator, name="tablocalculator"),

    path('cat/selftablo/', home_views.selftablo, name="selftablo"),
    path('cat/selftablo/ketan/', selftablo_views.ketan, name="selftabloketan"),
    path('cat/selftablo/modular/', selftablo_views.modular, name="selftablomodular"),
    path('cat/selftablo/calculator/', selftablo_views.calculator, name="selftablocalculator"),


    path('cat/exclusive/', home_views.exclusive, name="exclusive"),
    path('cat/exclusive/portfolio/', exclusive_views.portfolio, name="exclusiveportfolio"),

    path('cat/skinali/', home_views.skinali, name="skinali"),
    path('cat/skinali/portfolio/', skinali_views.portfolio, name="skinaliportfolio"),

    path('cat/evdekor/', home_views.evdekor, name="evdekor"),
    path('cat/evdekor/portfolio/', evdekor_views.portfolio, name="evdekorportfolio"),

    path('contact/', home_views.contact, name="contact"),
    path('about/', home_views.about, name="about"),
    path('search/', home_views.search, name="search"),
    path('filter/<int:id>/', home_views.filter, name="filter"),
    path('otaq/<int:id>/', home_views.filterotaq, name="filterotaq"),
    path('reng/<int:id>/', home_views.filterreng, name="filterreng"),
    path('', home_views.index, name="shipping"),
    path('category/<int:id>/', product_views.main_category, name="category"),
    path('product/<int:id>/', product_views.product, name="product"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

