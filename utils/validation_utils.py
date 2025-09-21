from email_validator import validate_email, EmailNotValidError
import logging

# Configure logging (optional but recommended)
logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    """
        Validate an email address using email-validator library.
            
                Args:
                        email (str): Email address to validate.
                            
                                Returns:
                                        bool: True if valid, False if not.
                                            """
                                                try:
                                                        # Validate and get normalized form of email
                                                                valid = validate_email(email)
                                                                        normalized_email = valid.email
                                                                                return True
                                                                                    except EmailNotValidError as e:
                                                                                            # Log the error for debugging (optional)
                                                                                                    logger.error(f"Invalid email {email}: {str(e)}")
                                                                                                            return False
                                                                                                            