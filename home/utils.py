from datetime import datetime, time

def is_restaurant_open():
    """
        Returns True if the restaurant is open (Mon-Fri, 9:00 AM to 10:00 PM), else False.
            """
                now = datetime.now()  # Use timezone-aware datetimes if your project uses them
                    weekday = now.weekday()  # Monday is 0, Sunday is 6

                        # Define operating days (Monday to Friday) and hours
                            operating_days = range(0, 5)  # 0-4 are Monday to Friday
                                opening_time = time(hour=9, minute=0)
                                    closing_time = time(hour=22, minute=0)  # 10 PM

                                        if weekday in operating_days:
                                                if opening_time <= now.time() < closing_time:
                                                            return True
                                                                return False