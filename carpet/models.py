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
    icon = models.FileField(null=True,blank=True)
    icon_class = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

 



class Color(models.Model):
    name = models.CharField(max_length=255)
    color_code = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Product(models.Model):
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    name = models.CharField(max_length=250, default="SKINALI ")
    code = models.CharField(max_length=250, null=True,blank=True)
    price = models.FloatField(default=30)
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