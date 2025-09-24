 from django.test import TestCase
 from decimal import Decimal
 from orders.models import Order, OrderItem
 from home.models import MenuItem
 from django.contrib.auth.models import User

 class OrderModelTest(TestCase):
     def setUp(self):
             user = User.objects.create_user(username='tester', password='pass')
                     self.menu_item = MenuItem.objects.create(name='Burger', price=Decimal('5.00'))
                             self.order = Order.objects.create(user=user)

                                 def test_calculate_total(self):
                                         OrderItem.objects.create(
                                                     order=self.order, menu_item=self.menu_item, quantity=2, price=Decimal('5.00')
                                                             )
                                                                     OrderItem.objects.create(
                                                                                 order=self.order, menu_item=self.menu_item, quantity=1, price=Decimal('5.00')
                                                                                         )

                                                                                                 total = self.order.calculate_total()
                                                                                                         self.assertEqual(total, Decimal('15.00'))
                                                                                                         