import datetime
from home.models import DailyOperatingHours

def get_today_operating_hours():
    """
        Returns a tuple of (open_time, close_time) for today's operating hours.
            If no entry is found for today, returns (None, None).
                """
                    # Get current day name, e.g., 'Monday'
                        today_name = datetime.datetime.today().strftime('%A')

                            try:
                                    # Assuming 'day' is a CharField on DailyOperatingHours with full day names (e.g., 'Monday')
                                            hours = DailyOperatingHours.objects.get(day=today_name)
                                                    return (hours.open_time, hours.close_time)
                                                        except DailyOperatingHours.DoesNotExist:
                                                                # No entry means closed or not set
                                                                        return (None, None)