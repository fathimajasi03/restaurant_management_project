# home/utils.py

def estimate_table_turnover_time(table_capacity):
    """
        Estimate dining duration for a table in minutes based on its seating capacity.

            Args:
                    table_capacity (int): Number of seats at the table.

                        Returns:
                                int: Estimated turnover time in minutes.
                                    """
                                        if table_capacity <= 2:
                                                return 60
                                                    elif table_capacity <= 4:
                                                            return 90
                                                                else:
                                                                        return 120