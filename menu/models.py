class Category(models.Model):
        category_name = models.CharField(max_length=100)

            def __str__(self):
                    return self.category_name

                    class MenuItem(models.Model):
                        name = models.CharField(max_length=255)
                            category = models.ForeignKey(Category, on_delete=models.CASCADE)
                                price = models.DecimalField(max_digits=6, decimal_places=2)
                                    # other fields...
                                    