from django.contrib import admin
from cadastro.models import Country, State, Cidade

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Cidade)
