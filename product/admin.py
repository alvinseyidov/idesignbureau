from django.contrib import admin
from .models import *
from evdekor.models import *
from exclusive.models import *
from fotooboy.models import *
from selftablo.models import *
from skinali.models import *
from tablo.models import *

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Color)
admin.site.register(SubCategory)
admin.site.register(Material)
admin.site.register(Interier)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    inlines = (ProductImageInline,)



class EvDekorProductImageInline(admin.TabularInline):
    model = EvDekorProductImage
    extra = 1

@admin.register(EvDekorProduct)
class EvDekorProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    inlines = (EvDekorProductImageInline,)


class FotoOboyProductImageInline(admin.TabularInline):
    model = FotoOboyProductImage
    extra = 1

@admin.register(FotoOboyProduct)
class FotoOboyProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    inlines = (FotoOboyProductImageInline,)

class ExclusiveProductImageInline(admin.TabularInline):
    model = ExclusiveProductImage
    extra = 1

@admin.register(ExclusiveProduct)
class ExclusiveProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    inlines = (ExclusiveProductImageInline,)

class SelfTabloProductImageInline(admin.TabularInline):
    model = SelfTabloProductImage
    extra = 1

@admin.register(SelfTabloProduct)
class SelfTabloProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    inlines = (SelfTabloProductImageInline,)

class SkinaliProductImageInline(admin.TabularInline):
    model = SkinaliProductImage
    extra = 1

@admin.register(SkinaliProduct)
class SkinaliProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    inlines = (SkinaliProductImageInline,)

class TabloProductImageInline(admin.TabularInline):
    model = TabloProductImage
    extra = 1

@admin.register(TabloProduct)
class TabloProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    inlines = (TabloProductImageInline,)



