Args:
    reviews_queryset (QuerySet): A Django QuerySet containing review objects with a numeric 'rating' field.

    Returns:
        float: The average rating, or 0.0 if there are no reviews or if input is invalid.
        """
        try:
            total_reviews = reviews_queryset.count()
                if total_reviews == 0:
                        return 0.0

                            # Sum all ratings efficiently; assumes 'rating' is numeric
                                total_rating = reviews_queryset.aggregate(total_sum=models.Sum('rating'))['total_sum'] or 0
                                    return float(total_rating) / float(total_reviews)
                                    except Exception:
                                        # Graceful fallback for unexpected input
                                            return 0.0 