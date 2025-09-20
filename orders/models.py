from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

        def __str__(self):
                return self.name


                class Order(models.Model):
                    # Add all necessary fields below with consistent 4 space indentation
                        customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
                            products = models.ManyToManyField('Product')  # example field, replace with your actual models
                                total_price = models.DecimalField(max_digits=10, decimal_places=2)
                                    order_date = models.DateTimeField(auto_now_add=True)

                                        status = models.ForeignKey(
                                                OrderStatus,
                                                        on_delete=models.SET_NULL,
                                                                null=True
                                                                    )

                                                                        def __str__(self):
                                                                                return f"Order #{self.id} by {self.customer}"
                                                                                