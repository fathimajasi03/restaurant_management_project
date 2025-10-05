from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=8, decimal_places=2)
            discount_percentage = models.DecimalField(
                    max_digits=4, decimal_places=2, default=0.00,
                            help_text="Discount as a decimal fraction, e.g. 0.10 for 10% off"
                                )
                                    # other relevant fields ...

                                        def get_final_price(self):
                                                discount = float(self.discount_percentage)
                                                        original_price = float(self.price)
                                                                final_price = original_price * (1 - discount)
                                                                        return max(final_price, 0.0)