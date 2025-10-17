from django.db import models

class MenuItem(models.Model):
    # existing fields...
        name = models.CharField(max_length=100)
            description = models.TextField()
                price = models.DecimalField(max_digits=8, decimal_places=2)
                    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
                        category = models.ForeignKey('MenuCategory', on_delete=models.CASCADE, related_name='menu_items')

                            # New allergens field for dietary info
                                allergens = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated list of allergens")

                                    def __str__(self):
                                            base_str = f"{self.name} - {self.category.name}"
                                                    if self.allergens:
                                                                base_str += f" (Allergens: {self.allergens})"
                                                                        return base_str