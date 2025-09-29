from django.db import models
from django.contrib.auth.models import User  # Or your custom user model
from .models import MenuItem  # Adjust import if MenuItem is elsewhere

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
        menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='reviews')
            rating = models.IntegerField()
                comment = models.TextField()
                    review_date = models.DateTimeField(auto_now_add=True)

                        def __str__(self):
                                return f"Review by {self.user.username} on {self.menu_item.name} ({self.rating} stars)"
                                