from django.db import models


class General(models.Model):
    main_image = models.ImageField()
    main_image_url = models.CharField(max_length=255)

    def __str__(self):
        return f"General Informations"


class Client(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Social(models.Model):
    icon = models.ImageField()
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    productcode = models.CharField(max_length=255)
    product = models.CharField(max_length=255, null=True, blank=True)
    telefon = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Sifarişlər'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.telefon} - {self.product}'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()

    class Meta:
        verbose_name = 'Yazılan Mesajlar'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name} - {self.phone}'