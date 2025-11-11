from datetime import datetime
from home.models import DailyOperatingHours  # adjust import path as needed

def is_reservation_time_valid(proposed_datetime: datetime) -> bool:
    """
        Checks if the proposed reservation datetime falls within the restaurant's operating hours on that day.

            Args:
                    proposed_datetime (datetime): The desired reservation date and time.

                        Returns:
                                bool: True if within operating hours, False otherwise.
                                    """
                                        weekday = proposed_datetime.strftime('%A')  # full weekday name e.g. 'Monday'
                                            
                                                try:
                                                        operating_hours = DailyOperatingHours.objects.get(day=weekday)
                                                            except DailyOperatingHours.DoesNotExist:
                                                                    return False  # No operating hours configured for the day

                                                                        # Extract the time component of the proposed datetime
                                                                            proposed_time = proposed_datetime.time()

                                                                                # Validate if proposed_time is strictly between open_time and close_time
                                                                                    if operating_hours.open_time < proposed_time < operating_hours.close_time:
                                                                                            return True
                                                                                                else:
                                                                                                        return False