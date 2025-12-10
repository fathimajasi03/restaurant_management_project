# home/models.py
from django.db import models

class Restaurant(models.Model):
    # ... existing fields ...
        street_address = models.CharField(max_length=255)
            city = models.CharField(max_length=100)
                state = models.CharField(max_length=100)
                    zip_code = models.CharField(max_length=20)
                        
                            def get_full_address(self):
                                    """
                                            Returns the complete formatted address as a single string.
                                                    """
                                                            address_parts = [self.street_address, self.city, self.state, self.zip_code]
                                                                    # Filter out empty values and join with commas
                                                                            formatted_parts = [part.strip() for part in address_parts if part.strip()]
                                                                                    return ', '.join(formatted_parts)