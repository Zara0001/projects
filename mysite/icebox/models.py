from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    count = models.CharField(max_length=10)
    date = models.CharField(max_length=16)

    def __str__(self):
        return self.name
