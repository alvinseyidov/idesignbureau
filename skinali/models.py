from django.db import models
from product.models import *

class SkinaliProduct(models.Model):
    main_category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="skinaliproducts", null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, related_name="skinaliproducts", null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, related_name="skinaliproducts", null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name="skinaliproducts", null=True, blank=True)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    discount_price = models.FloatField(blank=True, null=True)
    order_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'product'
        verbose_name = 'Məhsullar - SKİNALİ'
        verbose_name_plural = 'Məhsullar - SKİNALİ'

class SkinaliProductImage(models.Model):
    image = models.ImageField()
    is_main = models.BooleanField(default=False)
    product = models.ForeignKey(SkinaliProduct, on_delete=models.CASCADE, related_name="images")

    class Meta:
        app_label = 'product'