from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
        address = models.TextField()
            phone_number = models.CharField(max_length=20)
                opening_hours = models.CharField(max_length=255)  # e.g., "9 AM - 9 PM"
                    # add other important fields as needed

                        def __str__(self):
                                return self.name
                                