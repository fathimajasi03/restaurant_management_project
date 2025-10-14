def calculate_discount(price, discount_percentage):
        """
            Returns the discounted price given the original price and a discount percentage.

                Args:
                        price (float/int): The original price of the item.
                                discount_percentage (float/int): The discount percentage (e.g., 10 for 10%).

                                    Returns:
                                            float: The discounted price, rounded to 2 decimals.
                                                    If inputs are invalid, returns the original price (no discount).
                                                        """
                                                            try:
                                                                    price = float(price)
                                                                            discount_percentage = float(discount_percentage)
                                                                                    if price < 0 or discount_percentage < 0 or discount_percentage > 100:
                                                                                                raise ValueError("Price and discount must be non-negative, discount no more than 100%.")
                                                                                                        discount_amount = price * (discount_percentage / 100)
                                                                                                                return round(price - discount_amount, 2)
                                                                                                                    except (ValueError, TypeError):
                                                                                                                            # Handle invalid input gracefully
                                                                                                                                    return float(price) if isinstance(price, (int, float)) else 0.0