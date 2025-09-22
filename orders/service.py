from orders.models import Order

# Retrieve active orders using the custom manager
active_orders = Order.active_orders.get_active_orders()

for order in active_orders:
    print(order.id, order.status)
    