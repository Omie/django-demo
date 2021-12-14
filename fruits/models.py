from django.db import models

class FruitCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(max_length=50)

    color = models.CharField(max_length=30)

    category = models.ForeignKey(FruitCategory, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



