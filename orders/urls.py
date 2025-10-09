from django.test import TestCase
from .models import Order

class OrderRevenueTest(TestCase):
    def setUp(self):
            Order.objects.create(status='completed', total_amount=50)
                    Order.objects.create(status='completed', total_amount=75.5)
                            Order.objects.create(status='pending', total_amount=30)

                                def test_calculate_total_revenue(self):
                                        revenue = Order.calculate_total_revenue()
                                                self.assertEqual(revenue, 125.5)