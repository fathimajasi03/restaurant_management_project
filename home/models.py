from django.db import models

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255)
        email = models.EmailField()
            message = models.TextField()

                def __str__(self):
                        return f"Contact from {self.name} <{self.email}>"
                        