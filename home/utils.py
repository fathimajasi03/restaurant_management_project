# home/utils.py

from home.models import MenuItem, Cuisine

def get_distinct_cuisines():
    """
        Retrieve a list of all unique cuisine names available in the menu items.

            Returns:
                    list[str]: A list of unique cuisine names.
                        """
                            cuisine_names = MenuItem.objects.values_list('cuisine__name', flat=True).distinct()
                                return list(cuisine_names)