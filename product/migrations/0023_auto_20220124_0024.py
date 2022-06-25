# Generated by Django 3.2 on 2022-01-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_material_texture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='texture_image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='material',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]