from django.contrib import admin
from .models import *
 




admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Room)
admin.site.register(Color)

 

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    inlines = (ProductImageInline,)


 



