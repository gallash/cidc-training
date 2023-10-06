from django.urls import path
from cadastro.views import (
    states_and_cities,
    list_cities,
    detailed_cities_qs,
    detailed_cities_param,
    create_city,
    delete_city,
    update_city,
    list_states,
    detailed_state,
    create_state,
    delete_state,
)

# .../<int:id>/ is declaring that there will be an integer
# that will be named 'id' in the view function, that is
# required
urlpatterns = [
    path('', states_and_cities, name='states_and_cities'),
    path('cities/', list_cities, name='cities'),
    path('cities/details_qs/', detailed_cities_qs, name='detailed_cities_qs'),
    path('cities/details_param/<int:city_id>/', detailed_cities_param, name='detailed_cities_param'),
    path('cities/create/', create_city, name='create_city'),
    path('cities/delete/<int:city_id>', delete_city, name='delete_city'),
    path('cities/update/<int:city_id>', update_city, name='update_city'),
    path('states/', list_states, name='states'),
    path('states/details/<int:state_id>', detailed_state, name='details_state'),
    path('states/create/', create_state, name='create_state'),
    path('states/delete/<int:state_id>', delete_state, name='delete_state'),
]
