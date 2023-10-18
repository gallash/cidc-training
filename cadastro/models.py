from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        """
        For more information,
        https://docs.djangoproject.com/en/4.2/ref/models/options/
        """
        ordering = ['name']
        verbose_name_plural = 'Countries'


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    is_capital = models.BooleanField(default=False)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=False)
    description = models.TextField(verbose_name="Description", null=True, blank=False)

    def __str__(self):
        # Text representation of the object
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Cities'
