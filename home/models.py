from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
        rating = models.PositiveSmallIntegerField()  # e.g., 1 to 5 stars
            text = models.TextField(blank=True)
                created_at = models.DateTimeField(auto_now_add=True)

                    def __str__(self):
                            return f"Review by {self.user.username} - Rating: {self.rating}"