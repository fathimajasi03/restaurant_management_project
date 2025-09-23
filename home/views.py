from home.utils import send_email

def some_view(request):
    result = send_email(
            recipient_email="test@example.com",
                    subject="Welcome!",
                            message_body="Thank you for contacting us."
                                )
                                    # result is a dict: {'success': True/False, 'message': "..."}
                                    