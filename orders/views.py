from orders.models import Order
pending_orders = Order.orders.get_by_status('pending')
for order in pending_orders:
    print(order.id, order.status)
    