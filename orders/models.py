from django.db import models

class OrderManager(models.Manager):
    def get_by_status(self, status):
            return self.get_queryset().filter(status=status)
            
            class Order(models.Model):
                STATUS_CHOICES = [
                        ('pending', 'Pending'),
                                ('processing', 'Processing'),
                                        ('completed', 'Completed'),
                                            ]
                                            
                                                user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
                                                    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
                                                        # other fields...
                                                        
                                                            objects = models.Manager()  # Default manager
                                                                orders = OrderManager()  # Custom manager
                                                                                                                                                                                                                                                                    order = models.ForeignKey(Or                