import logging
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException

logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, customer_name, order_details):
    subject = f"Order Confirmation - Order #{order_id}"
        from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [customer_email]

                message = f"""
                Dear {customer_name},

                Thank you for your order #{order_id}!

                Here are your order details:

                {order_details}

                We appreciate your business.

                Best regards,
                Your Company Name
                """

                    try:
                            send_mail(
                                        subject=subject,
                                                    message=message,
                                                                from_email=from_email,
                                                                            recipient_list=recipient_list,
                                                                                        fail_silently=False
                                                                                                )
                                                                                                        return {'success': True, 'message': 'Order confirmation email sent successfully.'}
                                                                                                            except SMTPException as smtp_ex:
                                                                                                                    logger.error(f"SMTP error when sending order confirmation email: {smtp_ex}")
                                                                                                                            return {'success': False, 'message': 'Failed to send order confirmation email due to SMTP error.'}
                                                                                                                                except Exception as ex:
                                                                                                                                        logger.error(f"Unexpected error when sending order confirmation email: {ex}")
                                                                                                                                                return {'success': False, 'message': 'Failed to send order confirmation email due to an unexpected error.'}
                                                                                                                                                