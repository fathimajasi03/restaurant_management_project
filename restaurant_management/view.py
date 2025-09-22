from yourapp.models import Restaurant

# Create a new restaurant with operating days
r = Restaurant(name="Test Diner", operating_days="Mon,Tue,Wed,Thu,Fri")
r.save()

# Fetch and print
print(Restaurant.objects.get(id=r.id).operating_days)
