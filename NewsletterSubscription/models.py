# newsletter/models.py
from django.db import models

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)

        def __str__(self):
                return self.email

                # newsletter/admin.py
                from django.contrib import admin
                from .models import NewsletterSubscription

                @admin.register(NewsletterSubscription)
                class NewsletterSubscriptionAdmin(admin.ModelAdmin):
                    list_display = ('email', )