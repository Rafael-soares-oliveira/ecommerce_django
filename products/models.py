from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
import os
from django.conf import settings
from PIL import Image
from collections import defaultdict
from django.forms import ValidationError


class Products(models.Model):
    product_name = models.CharField(
        max_length=255,
        verbose_name=_('Product Name')
    )
    short_description = models.TextField(
        max_length=255,
        verbose_name=_('Short Description')
    )
    long_description = models.TextField(
        verbose_name=_('Long Description')
    )
    product_image = models.ImageField(
        upload_to='products_image/%Y/%m/',
        blank=True, null=True,
        verbose_name=_('Product Image')
    )
    slug = models.SlugField(unique=True)
    price_marketing = models.FloatField(
        default=0,
        verbose_name=_('Price Marketing')
    )
    price_marketing_offer = models.FloatField(
        default=0,
        verbose_name=_('Price Marketing Offer')
    )
    product_type = models.CharField(
        default='V',
        max_length=1,
        verbose_name=_('Product Type'),
        choices=(
            ('V', 'Variable'),
            ('S', 'Simple'),
        )
    )

    def __str__(self) -> str:
        return self.product_name

    # Resize image
    @staticmethod
    def resize_image(image, new_width=800):
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        if original_width <= new_width:
            image_pillow.close()
            return

        new_height = round(new_width * original_height / original_width)
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

        saved = super().save(*args, **kwargs)

        if self.product_image:
            try:
                self.resize_image(self.product_image, 800)
            except FileNotFoundError:
                ...

        return saved

    # Return error when two products have the same name
    def clean(self, *args, **kwargs):
        error_messages = defaultdict(list)
        products_from_db = Products.objects.filter(
            name__iexact=self.product_name).first()
        if products_from_db:
            if products_from_db.pk != self.pk:
                error_messages['name'].append(
                    _('Found products with the same name')
                )

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Variation(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name=_('Product')
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    price = models.FloatField(
        default=0,
        verbose_name=_('Price')
    )
    price_offer = models.FloatField(
        default=0,
        verbose_name=_('Price Offer')
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Stock')
    )

    def __str__(self) -> str:
        return self.name