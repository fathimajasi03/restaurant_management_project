import string
import secrets
from typing import Optional
from .models import Coupon  # Ensure Coupon model exists with a unique 'code' field

def generate_coupon_code(length: Optional[int] = 10) -> str:
    """
        Generate a unique alphanumeric coupon code of given length.
            
                Args:
                        length (int): Length of the coupon code. Default is 10.
                            
                                Returns:
                                        str: Unique coupon code.
                                            """
                                                characters = string.ascii_uppercase + string.digits
                                                    max_attempts = 1000  # fail-safe to prevent infinite loop
                                                        
                                                            for _ in range(max_attempts):
                                                                    code = ''.join(secrets.choice(characters) for _ in range(length))
                                                                            if not Coupon.objects.filter(code=code).exists():
                                                                                        return code
                                                                                            raise ValueError("Unable to generate a unique coupon code after many attempts")
                                                                                            