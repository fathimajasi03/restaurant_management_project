from django.test import TestCase
from django.contrib.auth.models import User
from orders.models import Order

class OrderManagerTest(TestCase):
    def setUp(self):
            user = User.objects.create(username='tester')
                    Order.objects.create(user=user, status='pending')
                            Order.objects.create(user=user, status='completed')

                                def test_get_by_status(self):
                                        pending_orders = Order.orders.get_by_status('pending')
                                                self.assertEqual(pending_orders.count(), 1)
                                                        self.assertEqual(pending_orders[0].status, 'pending')
                                                        