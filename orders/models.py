from django.db import models
status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

# Create your models here.
