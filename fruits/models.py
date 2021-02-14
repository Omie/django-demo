from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=50)

    color = models.CharField(max_length=30)

    def __str__(self):
        return self.name



