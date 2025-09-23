import string
import secrets
from orders.models import Order

def generate_unique_order_id(length=8):
    """
        Generate a unique short alphanumeric ID for orders.
            
                Args:
                        length (int): Length of the generated ID. Default is 8.
                            
                                Returns:
                                        str: The unique order ID.
                                            """
                                                chars = string.ascii_letters + string.digits
                                                    while True:
                                                            new_id = ''.join(secrets.choice(chars) for _ in range(length))
                                                                    if not Order.objects.filter(order_id=new_id).exists():
                                                                                return new_id
                                                                                