# Generated by Django 3.2 on 2022-01-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
