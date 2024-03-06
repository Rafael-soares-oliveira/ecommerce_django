from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
import os
from django.conf import settings
from PIL import Image
from utils.convert_str import convert_str


class Product(models.Model):
    product_name = models.CharField(
        max_length=55,
        unique=True,
        verbose_name=_('Name')
    )
    slug = models.SlugField(
        max_length=255,
        unique=True
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
    product_type = models.CharField(
        default='V',
        max_length=1,
        verbose_name=_('Product Type'),
        choices=(
            ('V', _('Variable')),
            ('S', _('Simple')),
        )
    )

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

    def get_short_name(self):
        return f'{(self.product_name)[:55]}...'

    # slugify the product name / resize image
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.product_name)}'
            self.slug = slug

        super().save(*args, **kwargs)

    def get_min_price(self):
        price = ProductVariation.objects.filter(
            product_id__exact=self.pk).values(
                'price').aggregate(models.Min('price'))['price__min']
        return price

    def get_price(self):
        price = self.get_min_price()
        return convert_str(price)
    get_price.short_description = _('Base Price')

    def get_min_offer_price(self):
        price_offer = ProductVariation.objects.filter(
            product_id__exact=self.pk, offer_price__gt=0).values(
                'offer_price').aggregate(
                    models.Min('offer_price'))['offer_price__min']
        if price_offer is None:
            return 0
        else:
            return price_offer

    def get_offer_price(self):
        price = self.get_min_offer_price()
        return convert_str(price)
    get_offer_price.short_description = _('Base Offer Price')

    def __str__(self) -> str:
        return self.product_name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductVariation(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variations',
        verbose_name=_('Product')
    )
    variation_name = models.CharField(
        max_length=50,
        default="",
        verbose_name=_('Variation Name')
    )
    slug = models.SlugField(
        max_length=65,
        default='',
    )
    price = models.FloatField(
        default=0,
        verbose_name=_('Price')
    )
    offer_price = models.FloatField(
        default=0,
        verbose_name=_('Offer Price')
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Stock')
    )

    def get_price(self):
        return convert_str(self.price)

    def get_offer_price(self):
        return convert_str(self.offer_price)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.variation_name)}'
            self.slug = slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product Variation')
        verbose_name_plural = _('Product Variations')
