# account/models.py
from django.db import models

class CustomerProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
        phone_number = models.CharField(max_length=20)
            delivery_address = models.TextField()

                def get_full_name(self):
                        first_name = self.user.first_name or ''
                                last_name = self.user.last_name or ''
                                        full_name = f"{first_name} {last_name}".strip()
                                                return full_name if full_name else ''