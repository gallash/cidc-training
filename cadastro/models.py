from django.db import models


# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    is_capital = models.BooleanField(default=False)

    def __str__(self):
        # Text representation of the object
        return self.nome


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
