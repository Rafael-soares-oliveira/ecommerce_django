# Generated by Django 5.0.1 on 2024-03-05 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_price_alter_productvariation_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='Preço Base'),
        ),
    ]
