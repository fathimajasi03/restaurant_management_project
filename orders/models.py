from django.db import models
class Order(models.Model):
    unique_id = models.CharField(max_length=16, unique=True)
        status = models.CharField(max_length=20)