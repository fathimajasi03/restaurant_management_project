import logging
from .models import Order

logger = logging.getLogger(__name__)

def update_order_status(order_id, new_status):
    """
        Update the status of an order by its ID.

            Args:
                    order_id (int): Primary key of the order to update.
                            new_status (str): New status value.

                                Returns:
                                        tuple: (success, message)
                                                    success (bool): True if updated, False otherwise.
                                                                message (str): Info or error string.
                                                                    """
                                                                        try:
                                                                                order = Order.objects.get(id=order_id)
                                                                                    except Order.DoesNotExist:
                                                                                            logger.error(f"Order with ID {order_id} not found.")
                                                                                                    return False, "Order not found."

                                                                                                        old_status = order.status
                                                                                                            order.status = new_status
                                                                                                                order.save()
                                                                                                                    logger.info(f"Order {order_id} status changed from {old_status} to {new_status}.")
                                                                                                                        return True, f"Order status updated to {new_status}."
                                                                                                                        