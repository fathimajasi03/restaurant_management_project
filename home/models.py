from django.db import models

class MenuItem(models.Model):
    # ... existing fields ...
        is_gluten_free = models.BooleanField(
                default=False,
                        help_text='Indicates if the menu item is gluten-free.'
                            )