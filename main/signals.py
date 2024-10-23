from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from products.models import Products
from .models import Movements


@receiver(post_save, sender=Products)
def log_product_creation(sender, instance, created, **kwargs):
    if created:
        Movements.objects.create(
            product=instance,
            movement_type='Создание товара',
            quantity_change=instance.quantity
        )


