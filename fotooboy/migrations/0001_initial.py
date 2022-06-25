# Generated by Django 3.2 on 2022-01-20 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0018_auto_20220118_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('is_featured', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('order_count', models.PositiveIntegerField(default=0)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotooboyproducts', to='product.color')),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotooboyproducts', to='product.category')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotooboyproducts', to='product.room')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotooboyproducts', to='product.subcategory')),
            ],
        ),
    ]