from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
        # other existing fields...
            is_featured = models.BooleanField(default=False)  # new field to highlight featured dishes

                def __str__(self):
                        return self.name