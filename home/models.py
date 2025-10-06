from django.db import models
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
        image = models.URLField(blank=True)