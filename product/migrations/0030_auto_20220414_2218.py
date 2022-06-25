# Generated by Django 3.2 on 2022-04-14 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_alter_product_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('lang', models.CharField(choices=[('az', 'az'), ('ru', 'ru'), ('en', 'en')], max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('name',)},
        ),
    ]