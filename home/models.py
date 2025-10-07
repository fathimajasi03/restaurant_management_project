from django.db import models
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    class MenuItem(models.Model):
        name = models.CharField(max_length=100)
            price = models.DecimalField(max_digits=8,decimal_places=2)
                description = models.TextField()
                    category = models.ForeignKey(MenuCategory,on_delete=models.CASCADE)