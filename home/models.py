from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    # ... existing fields

    class UserReviews(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
            menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="reviews")
                rating = models.IntegerField()
                    comment = models.TextField(blank=True)
                        created_at = models.DateTimeField(auto_now_add=True)

                            def __str__(self):
                                    return f"{self.user.username} review for {self.menu_item.name}: {self.rating} stars"