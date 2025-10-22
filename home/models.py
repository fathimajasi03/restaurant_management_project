from django.db import models
from django.utils import timezone

# Assuming your menu model is called MenuItem. 
# If it's RestaurantMenu, change MenuItem to RestaurantMenu where relevant.

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
        # ... other fields ...

            def is_daily_special(self):
                    today = timezone.localdate()
                            return DailySpecial.objects.filter(menu_item=self, date=today).exists()

                                def __str__(self):
                                        return self.name

                                        class DailySpecial(models.Model):
                                            menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
                                                date = models.DateField()

                                                    class Meta:
                                                            unique_together = (('menu_item', 'date'),)

                                                                def __str__(self):
                                                                        return f"Special: {self.menu_item} on {self.date}"