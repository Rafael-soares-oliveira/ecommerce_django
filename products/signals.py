from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from products.models import Product
import os


def delete_product_image(instance):
    try:
        os.remove(instance.product_image.path)
    except (ValueError, FileNotFoundError):
        ...


# Delete the product image when delete de product
@receiver(pre_delete, sender=Product)
def product_image_delete(sender, instance, *args, **kwargs):
    old_instance = Product.objects.filter(pk=instance.pk).first()
    if old_instance:
        delete_product_image(old_instance)


# Delete the old product image when change the image
@receiver(pre_save, sender=Product)
def product_image_update(sender, instance, *args, **kwargs):
    old_instance = Product.objects.filter(pk=instance.pk).first()
    if not old_instance:
        return

    is_new_cover = old_instance.product_image != instance.product_image
    if is_new_cover:
        delete_product_image(old_instance)
