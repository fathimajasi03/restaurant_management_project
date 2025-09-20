import string
import secrets
from typing import Optional
from .models import Coupon  # Replace with your actual Coupon model


class CouponCodeGenerationError(Exception):
    pass


    def generate_coupon_code(length: Optional[int] = 10, max_attempts: int = 1000) -> str:
        characters = string.ascii_uppercase + string.digits

            for _ in range(max_attempts):
                    potential_code = ''.join(secrets.choice(characters) for _ in range(length))

                            if not Coupon.objects.filter(code=potential_code).exists():
                                        return potential_code

                                            raise CouponCodeGenerationError(
                                                    f"Failed to generate a unique coupon code after {max_attempts} attempts. "
                                                            "Consider increasing `length` or `max_attempts`."
                                                                )
                                                                
                                                                