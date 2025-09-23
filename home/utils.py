import logging
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException

logger = logging.getLogger(__name__)

def send_email(recipient_email, subject, message_body):
    """
        Send an email to the given recipient.

            Args:
                    recipient_email (str): The email address of the recipient.
                            subject (str): The subject of the email.
                                    message_body (str): The message body of the email.

                                        Returns:
                                                dict: Contains success status and message.
                                                    """
                                                        try:
                                                                send_mail(
                                                                            subject=subject,
                                                                                        message=message_body,
                                                                                                    from_email=settings.DEFAULT_FROM_EMAIL,
                                                                                                                recipient_list=[recipient_email],
                                                                                                                            fail_silently=False,
                                                                                                                                    )
                                                                                                                                            return {"success": True, "message": "Email sent successfully."}
                                                                                                                                                except SMTPException as smtp_ex:
                                                                                                                                                        logger.error(f"SMTP error when sending email to {recipient_email}: {smtp_ex}")
                                                                                                                                                                return {"success": False, "message": "SMTP error occurred while sending the email."}
                                                                                                                                                                    except Exception as ex:
                                                                                                                                                                            logger.error(f"Error when sending email to {recipient_email}: {ex}")
                                                                                                                                                                                    return {"success": False, "message": "An unexpected error occurred while sending the email."}
                                                                                                                                                                                    