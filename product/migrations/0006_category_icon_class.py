# Generated by Django 3.2 on 2022-01-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_subcategory_icon_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon_class',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]