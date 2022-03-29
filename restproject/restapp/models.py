from django.db import models


class Item(models.Model):
    category = models.CharField(max_length=150)
    subcategory = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.name
