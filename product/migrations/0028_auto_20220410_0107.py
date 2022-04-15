# Generated by Django 3.2 on 2022-04-10 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_interier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=180),
        ),
    ]
