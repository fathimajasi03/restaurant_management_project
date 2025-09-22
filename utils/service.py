from your_app.utils.email_utils import send_order_confirmation_email

order_details_text = """
1x Cheeseburger - $5.99
2x Fries - $3.00
Total: $8.99
"""

result = send_order_confirmation_email(
    order_id=order.id,
        customer_email=order.user.email,
            customer_name=order.user.get_full_name(),
                order_details=order_details_text
                )

                if not result['success']:
                    # Log or handle failed email sending if necessary
                        print(result['message'])
                        