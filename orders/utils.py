import re

def is_valid_phone_number(phone_number):
    """
        Validate a phone number string against a basic pattern.
            
                Allows:
                    - 10 to 12 digits total
                        - Optional country code prefix starting with '+'
                            - Spaces or hyphens as separators
                                
                                    Args:
                                            phone_number (str): The phone number to validate
                                                
                                                    Returns:
                                                            bool: True if the phone number matches the pattern, False otherwise
                                                                """
                                                                    pattern = re.compile(r'^(+?d{1,3}[- ]?)?(d{3}[- ]?d{3}[- ]?d{4})$')
                                                                        return bool(pattern.match(phone_number))