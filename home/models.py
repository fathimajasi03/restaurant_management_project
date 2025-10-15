from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
        description = models.TextField()
            price = models.DecimalField(max_digits=8, decimal_places=2)
                image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
                    category = models.ForeignKey('MenuCategory', on_delete=models.CASCADE, related_name='menu_items')

                        def __str__(self):
                                return f"{self.name} - {self.category.name}"