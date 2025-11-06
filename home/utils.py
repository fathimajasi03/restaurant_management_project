from datetime import datetime

def format_datetime(dt):
    """
        Format a datetime object into a readable string like:
            'January 1, 2023 at 10:30 AM'.
                
                    If dt is None, returns an empty string.
                        
                            Args:
                                    dt (datetime or None): The datetime object to format.
                                        
                                            Returns:
                                                    str: Formatted datetime string or empty string if dt is None.
                                                        """
                                                            if dt is None:
                                                                    return ""
                                                                        # Format datetime using strftime with full month name, day, year, and 12-hour time with AM/PM
                                                                            return dt.strftime("%B %-d, %Y at %-I:%M %p")