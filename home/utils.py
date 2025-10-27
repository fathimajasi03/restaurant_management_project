# home/utils.py
import string
import random
from home.models import Reservation

def generate_reservation_confirmation_number(length=8):
    """
        Generate a unique alphanumeric reservation confirmation number.
            Checks against existing Reservation confirmation numbers to ensure uniqueness.
                """
                    characters = string.ascii_uppercase + string.digits

                        while True:
                                confirmation_number = ''.join(random.choices(characters, k=length))
                                        # Check uniqueness in Reservation model
                                                if not Reservation.objects.filter(confirmation_number=confirmation_number).exists():
                                                            return confirmation_number