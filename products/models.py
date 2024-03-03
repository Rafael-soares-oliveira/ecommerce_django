from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
import os
from django.conf import settings
from PIL import Image


class Product(models.Model):
    product_name = models.CharField(
        max_length=55,
        unique=True,
        verbose_name=_('Name')
    )
    short_description = models.TextField(
        max_length=255,
        verbose_name=_('Short Description')
    )
    long_description = models.TextField(
        verbose_name=_('Long Description')
    )
    product_image = models.ImageField(
        upload_to='media/product_image/%Y/%m/%d',
        blank=True,
        default='',
        verbose_name=_('Image')
    )
    slug = models.SlugField(
        max_length=255,
        unique=True)
    product_type = models.CharField(
        default='V',
        max_length=1,
        verbose_name=_('Product Type'),
        choices=(
            ('V', _('Variable')),
            ('S', _('Simple')),
        )
    )

    def get_short_name(self):
        return f'{(self.product_name)[:55]}...'

    # Resize image
    @staticmethod
    def resize_image(image, new_width=800, new_height=800):
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)
        new_image.save(
            image_full_path,
            optimize=True,
            quality=50,
        )

    # slugify the product name / resize image
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.product_name)}'
            self.slug = slug

        super().save(*args, **kwargs)

        if self.product_image:
            self.resize_image(self.product_image, 800)

    def __str__(self) -> str:
        return self.product_name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductVariation(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product')
    )
    variation_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Variation Name')
    )
    price = models.FloatField(
        default=0,
        verbose_name=_('Price')
    )
    offer_price = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_('Offer Price')
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Stock')
    )

    def get_price(self):
        return f'R$ {self.price:.2f}'.replace('.', ',')

    def get_offer_price(self):
        return f'R$ {self.offer_price:.2f}'.replace('.', ',')

    class Meta:
        verbose_name = _('Product Variation')
        verbose_name_plural = _('Product Variations')
