def calculate_discount_amount(order_total, discount_percentage):
        """
            Calculate discount amount from order total and discount percentage.

                Args:
                      order_total (float or int): The total order amount.
                            discount_percentage (float or int): The discount percentage (0-100).

                                Returns:
                                      float: The discount amount, or 0 if inputs are invalid.
                                          """
                                              try:
                                                      total = float(order_total)
                                                              discount = float(discount_percentage)
                                                                      if total < 0 or discount < 0 or discount > 100:
                                                                                  return 0
                                                                                          return total * (discount / 100)
                                                                                              except (ValueError, TypeError):
                                                                                                      return 0