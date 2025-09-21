from email_validator import validate_email, EmailNotValidError
import logging

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    try:
            valid = validate_email(email)
                    return True
                        except EmailNotValidError as e:
                                logger.error(f"Invalid email {email}: {str(e)}")
                                        return False
                                        