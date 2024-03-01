# Generated by Django 5.0.1 on 2024-03-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_complement',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Address Complement'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address_number',
            field=models.CharField(max_length=5, verbose_name='Address Number'),
        ),
    ]