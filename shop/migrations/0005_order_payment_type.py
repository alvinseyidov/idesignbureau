# Generated by Django 3.2 on 2022-04-25 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(default='Cash On Delivery', max_length=100),
        ),
    ]