from django.db import models

class Post(models.Model):
    text = models.TextField()

    # Adding a __str__ function impoves readability for the models.
    def __str__(self):
        return self.text[:50]
