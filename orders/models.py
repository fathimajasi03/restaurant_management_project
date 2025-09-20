from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

        def __str__(self):
                return self.name

                class Order(models.Model):
                    # your existing fields go here
                        
                            status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
                            
