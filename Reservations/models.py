from django.db import models
from datetime import timedelta, datetime

class Reservation(models.Model):
    reservation_start = models.DateTimeField()
        reservation_end = models.DateTimeField()
            # other fields like user, restaurant, etc.

                @classmethod
                    def find_available_slots(cls, start_time, end_time, slot_duration=timedelta(minutes=30)):
                            """
                                    Find available reservation slots in given time window.

                                            Args:
                                                        start_time (datetime): Start datetime of search window.
                                                                    end_time (datetime): End datetime of search window.
                                                                                slot_duration (timedelta): Length of each reservation slot.

                                                                                        Returns:
                                                                                                    list of (slot_start, slot_end) tuples representing available slots.
                                                                                                            """

                                                                                                                    # Get all reservations that overlap with the search interval
                                                                                                                            overlapping_reservations = cls.objects.filter(
                                                                                                                                        reservation_start__lt=end_time,
                                                                                                                                                    reservation_end__gt=start_time
                                                                                                                                                            ).values('reservation_start', 'reservation_end').order_by('reservation_start')

                                                                                                                                                                    # Build a timeline from start_time to end_time with slot_duration increments
                                                                                                                                                                            available_slots = []
                                                                                                                                                                                    current_slot_start = start_time

                                                                                                                                                                                            # Create a list of busy intervals
                                                                                                                                                                                                    busy_intervals = []
                                                                                                                                                                                                            for res in overlapping_reservations:
                                                                                                                                                                                                                        busy_intervals.append((res['reservation_start'], res['reservation_end']))

                                                                                                                                                                                                                                def is_slot_free(slot_start, slot_end):
                                                                                                                                                                                                                                            for busy_start, busy_end in busy_intervals:
                                                                                                                                                                                                                                                            # If slot overlaps any busy interval, it is not free
                                                                                                                                                                                                                                                                            if slot_start < busy_end and slot_end > busy_start:
                                                                                                                                                                                                                                                                                                return False
                                                                                                                                                                                                                                                                                                            return True

                                                                                                                                                                                                                                                                                                                    while current_slot_start + slot_duration <= end_time:
                                                                                                                                                                                                                                                                                                                                slot_end = current_slot_start + slot_duration
                                                                                                                                                                                                                                                                                                                                            if is_slot_free(current_slot_start, slot_end):
                                                                                                                                                                                                                                                                                                                                                            available_slots.append((current_slot_start, slot_end))
                                                                                                                                                                                                                                                                                                                                                                        current_slot_start = slot_end

                                                                                                                                                                                                                                                                                                                                                                                return available_slots
                                                                                                                                                                                                                                                                                                                                                                                