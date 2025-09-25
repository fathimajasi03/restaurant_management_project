   from django.db import models
   from django.contrib.auth.models import User
   
   class Order(models.Model):
       STATUS_CHOICES = [
               ('pending', 'Pending'),
                       ('processing', 'Processing'),
                               ('completed', 'Completed'),
                                   ]
                                       user = models.ForeignKey(User, on_delete=models.CASCADE)
                                           status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
                                               # other fields as needed
                                                                                                                 order = models.ForeignKey(Or                