from home.models import Table

def get_available_tables_by_capacity(num_guests):
    """
        Returns a QuerySet of available tables that can accommodate at least `num_guests` people.

            Args:
                    num_guests (int): The number of guests needing seating.

                        Returns:
                                QuerySet: Table objects where is_available is True and capacity >= num_guests.
                                    """
                                        return Table.objects.filter(is_available=True, capacity__gte=num_guests)