# Generated by Django 3.2 on 2022-01-20 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20220118_1408'),
        ('fotooboy', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='FotoOboyProduct',
        ),
    ]
