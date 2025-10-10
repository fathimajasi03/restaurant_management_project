import re

def format_phone_number(phone_str):
    """
        Format a phone number string as (XXX) XXX-XXXX.
            Handles numbers with or without country code.
                Returns cleaned/standardized string, or the input if invalid.
                    """
                        try:
                                # Remove non-digit characters
                                        digits = re.sub(r'D', '', phone_str)

                                                # Remove leading '1' (US country code), if present
                                                        if len(digits) == 11 and digits.startswith('1'):
                                                                    digits = digits[1:]

                                                                            if len(digits) != 10:
                                                                                        raise ValueError('Phone number must have 10 digits.')

                                                                                                return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
                                                                                                    except Exception as e:
                                                                                                            # Handle invalid input by returning the input as-is or a default string
                                                                                                                    return phone_str  # Or: f"Invalid: {phone_str}"