import re

def is_valid_email(email):
    """
        Validates an email address using a regex pattern.
            Returns True if valid, False otherwise.
                """
                    if not isinstance(email, str):
                            return False
                                pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
                                    return re.match(pattern, email) is not None