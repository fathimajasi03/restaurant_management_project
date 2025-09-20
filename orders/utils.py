import string
import secrets
from typing import Optional
from .models import Coupon  # Replace with your actual coupon model


class CouponCodeGenerationError(Exception):
    """Custom exception raised when unique coupon code generation fails."""
        pass


        def generate_coupon_code(length: Optional[int] = 10, max_attempts: int = 1000) -> str:
            """
                Generate a unique alphanumeric coupon code.

                    Args:
                            length (int): Length of the coupon code.
                                    max_attempts (int): Maximum attempts to generate a unique code.

                                        Returns:
                                                str: A unique coupon code.

                                                    Raises:
                                                            CouponCodeGenerationError: If unable to generate a unique code after max_attempts.
                                                                """
                                                                    characters = string.ascii_uppercase + string.digits

                                                                        for _ in range(max_attempts):
                                                                                potential_code = ''.join(secrets.choice(characters) for _ in range(length))

                                                                                        # Check for uniqueness in the Coupon table by code field
                                                                                                if not Coupon.objects.filter(code=potential_code).exists():
                                                                                                            return potential_code

                                                                                                                # Raise an informative error after too many attempts
                                                                                                                    raise CouponCodeGenerationError(
                                                                                                                            f"Failed to generate a unique coupon code after {max_attempts} attempts."
                                                                                                                                )
                                                                                                                                