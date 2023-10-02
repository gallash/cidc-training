from django.db import models

# Create your models here.
class Cidade(models.Model):

    nome = models.CharField(max_length=100)

    def __str__(self):
        # Defines a string that will serve to identify different objects in the DB
        return self.nome
