# Generated by Django 5.0.1 on 2024-03-05 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_product_price_remove_product_price_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.AddField(
            model_name='productvariation',
            name='product_image',
            field=models.ImageField(blank=True, default='', upload_to='media/product_image/%Y/%m/%d', verbose_name='Imagem'),
        ),
    ]
