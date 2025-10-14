from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order

@receiver(post_save, sender=Order)
def send_status_change_email(sender, instance, created, **kwargs):
    # Only trigger if status has changed (not on creation)
        if not created:
                # Fetch previous value from DB
                        old_instance = sender.objects.get(pk=instance.pk)
                                if old_instance.status != instance.status:
                                            subject = f"Order #{instance.id} Status Updated"
                                                        message = (f"Order #{instance.id} status changed from '{old_instance.status}' to '{instance.status}'.")
                                                                    send_mail(
                                                                                    subject,
                                                                                                    message,
                                                                                                                    settings.DEFAULT_FROM_EMAIL,
                                                                                                                                    [settings.RESTAURANT_ADMIN_EMAIL],  # Add this to your settings!
                                                                                                                                                )