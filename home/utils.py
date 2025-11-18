from datetime import datetime
from .models import DailyOperatingHours

def is_restaurant_open():
    # Get current day and time
        now = datetime.now()
            current_day = now.strftime('%A')  # Get the full weekday name (e.g., Monday, Tuesday, etc.)
                current_time = now.time()

                    # Query DailyOperatingHours model for the current day
                        try:
                                operating_hours = DailyOperatingHours.objects.get(day=current_day)
                                    except DailyOperatingHours.DoesNotExist:
                                            # If no operating hours are defined for the current day, assume the restaurant is closed
                                                    return False

                                                        # Compare current time with opening and closing times
                                                            opening_time = operating_hours.opening_time
                                                                closing_time = operating_hours.closing_time

                                                                    if opening_time <= current_time < closing_time:
                                                                            return True
                                                                                else:
                                                                                        return False