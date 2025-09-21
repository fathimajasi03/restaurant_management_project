"""
This module provides utility functions for validating data inputs.

Currently includes:
- Email address validation using the email-validator library.
"""

from email_validator import validate_email, EmailNotValidError
import logging

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    """
        Validate an email address.

            Args:
                    email (str): The email address to validate.

                        Returns:
                                bool: True if the email is valid, False otherwise.
                                    """
                                        try:
                                                validate_email(email)
                                                    except EmailNotValidError as e:
                                                            logger.error(f"Invalid email {email}: {str(e)}")
                                                                    return False
                                                                        return True
                                                                        