# Generated by Django 5.0.1 on 2024-03-05 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariation',
            name='product_image',
        ),
    ]
