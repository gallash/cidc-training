from django.urls import path
from cadastro.views import list_cities, detailed_cities_qs, detailed_cities_param

# .../<int:id>/ is declaring that there will be an integer
# that will be named 'id' in the view function, that is
# required
urlpatterns = [
    path('', list_cities, name='list_cities'),
    path('details_qs/', detailed_cities_qs, name='detailed_cities_qs'),
    path('details_param/<int:city_id>/', detailed_cities_param, name='detailed_cities_param')
]