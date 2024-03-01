from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from products.models import Product
import os


def delete_image(instance):
    try:
        os.remove(instance.image.path)
    except (ValueError, FileNotFoundError):
        ...


# Delete the product image when delete de product
@receiver(pre_delete, sender=Product)
def image_delete(sender, instance, *args, **kwargs):
    old_instance = Product.objects.filter(pk=instance.pk).first()
    if old_instance:
        delete_image(old_instance)


# Delete the old product image when change the image
@receiver(pre_save, sender=Product)
def image_update(sender, instance, *args, **kwargs):
    old_instance = Product.objects.filter(pk=instance.pk).first()
    if not old_instance:
        return

    is_new_image = old_instance.image != instance.image
    if is_new_image:
        delete_image(old_instance)
