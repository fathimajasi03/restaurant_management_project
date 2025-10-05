 def calculate_discount(original_price, discount_percentage):
        try:
                # Convert inputs to float for calculation
                        price = float(original_price)
                                discount = float(discount_percentage)
                                
                                        # Validate values
                                                if price < 0:
                                                            raise ValueError("Original price cannot be negative")
                                                                    if discount < 0 or discount > 1:
                                                                                raise ValueError("Discount percentage must be between 0 and 1")
                                                                                
                                                                                        # Calculate discounted price
                                                                                                discounted_price = price * (1 - discount)
                                                                                                        # Ensure discounted_price is not negative due to discount logic
                                                                                                                return max(discounted_price, 0)
                                                                                                                        
                                                                                                                            except (ValueError, TypeError) as e:
                                                                                                                                    # Return error message or None to indicate failure
                                                                                                                                            return f"Error: {str(e)}"             else:                     open_time = time(9, 0)