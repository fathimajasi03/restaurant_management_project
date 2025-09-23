 from django.db import models

 class Order(models.Model):
     order_id = models.CharField(max_length=16, unique=True)
         # other fields...
                        

                                              