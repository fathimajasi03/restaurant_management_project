def calculate_average_rating(reviews_queryset):
        """
            Calculate the average rating from a queryset of reviews.

                Args:
                        reviews_queryset (QuerySet): Django queryset containing reviews with a 'rating' field.

                            Returns:
                                    float: average rating, or 0.0 if no reviews available.
                                        """
                                            total_reviews = reviews_queryset.count()
                                                if total_reviews == 0:
                                                        return 0.0

                                                            total_rating = reviews_queryset.aggregate(total=models.Sum('rating'))['total'] or 0
                                                                average = total_rating / total_reviews
                                                                    return float(average)                                                      