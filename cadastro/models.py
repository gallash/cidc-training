from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    is_capital = models.BooleanField(default=False)

    def __str__(self):
        # Text representation of the object
        return self.nome
