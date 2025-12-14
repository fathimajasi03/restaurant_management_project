# orders/models.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reservation

@receiver(post_save, sender=Reservation)
def log_new_reservation(sender, instance, created, **kwargs):
    if created:
            print(f"New reservation created: ID #{instance.id} for {instance.customer_name} at {instance.time}")