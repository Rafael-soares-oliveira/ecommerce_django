from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )
    total = models.FloatField(
        verbose_name='Total'
    )
    status = models.CharField(
        max_length=1,
        default='C',
        verbose_name='Status',
        choices=[
            ('A', _('Approved')),
            ('C', _('Created')),
            ('R', _('Reproved')),
            ('P', _('Pending')),
            (_('E'), _('Sent')),
            ('F', _('Finished')),
        ]
    )

    def __str__(self) -> str:
        return f'Order N. {self.pk}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_('Order')
    )
    product = models.CharField(
        max_length=255,
        verbose_name=_('Product')
    )
    product_id = models.PositiveIntegerField(
        verbose_name=_('Product ID')
    )
    product_variation = models.CharField(
        max_length=255,
        verbose_name=_('Product Variation')
    )
    product_variation_id = models.PositiveIntegerField(
        verbose_name=_('Product Variation ID')
    )
    price = models.FloatField(
        verbose_name=_('Price')
    )
    offer_price = models.FloatField(
        default=0,
        verbose_name=_('Offer Price')
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_('Quantity')
    )
    product_image = models.CharField(
        max_length=2000,
        verbose_name=_('Product Image')
    )

    def __str__(self) -> str:
        return f' Ordem Item Number {self.order}'

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')
