from tkinter.tix import Tree
from django.db import models



class Tag(models.Model):
    LANG = (
        ("az","az"),
        ("ru","ru"),
        ("en","en"),
    )
    name = models.CharField(max_length=128, unique=True)
    #lang = models.CharField(max_length=2, choices=LANG)

    def __str__(self):
        return self.name

class Category(models.Model):
    icon = models.FileField()
    icon_class = models.CharField(max_length=255)
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    icon = models.FileField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="subs", null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=250)
    class Meta:
        ordering=('name',)	
    def __str__(self):
        return self.name



class Color(models.Model):
    name = models.CharField(max_length=255)
    color_code = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()

    def __str__(self):
        return self.name 

class Product(models.Model):
    main_category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", null=True, default=1)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250, null=True,blank=True)
    price = models.FloatField(default=180)
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    discount_price = models.FloatField(blank=True, null=True)
    order_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)

    def __str__(self):
        return self.name

    def save(self, request=False, *args, **kwargs):
        self.code = self.name
        super(Product, self).save(*args, **kwargs)

class ProductImage(models.Model):
    image = models.ImageField()
    is_main = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

class Interier(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name            
