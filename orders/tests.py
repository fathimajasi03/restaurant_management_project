from django.test import TestCase
from decimal import Decimal
from orders.models import Order, OrderItem
from home.models import MenuItem
from django.contrib.auth.models import User

class OrderTotalTest(TestCase):
    def setUp(self):
            user = User.objects.create(username="tester")
                    order = Order.objects.create(user=user)
                            product = MenuItem.objects.create(name="Pizza", price=Decimal("10.00"))
                                    OrderItem.objects.create(order=order, menu_item=product, quantity=2, price=Decimal("10.00"))
                                            OrderItem.objects.create(order=order, menu_item=product, quantity=3, price=Decimal("10.00"))
                                                    self.order = order

                                                        def test_calculate_total(self):
                                                                total = self.order.calculate_total()
                                                                        # first line: 2 * 10.00 = 20.00, second line: 3 * 9.00 = 27.00, grand total = 47.00
                                                                                self.assertEqual(total, Decimal("47.00"))
                                                                                