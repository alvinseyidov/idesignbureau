# Generated by Django 3.2 on 2022-04-14 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_alter_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='lang',
        ),
    ]
