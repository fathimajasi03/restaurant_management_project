from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
        cuisine = models.CharField(max_length=100)
            # other fields ...

                @classmethod
                    def get_items_by_cuisine(cls, cuisine_type):
                            """
                                    Returns a QuerySet of MenuItem objects filtered by the given cuisine_type.
                                            """
                                                    return cls.objects.filter(cuisine=cuisine_type)