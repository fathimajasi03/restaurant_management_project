from django.db import models

class MenuItem(models.Model):
    # existing fields ...
        name = models.CharField(max_length=100)
            # Add this new field:
                is_featured = models.BooleanField(
                        default=False,
                                help_text="Designates whether this menu item is featured"
                                    )

                                        def __str__(self):
                                                return self.name