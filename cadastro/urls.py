from django.urls import path
from cadastro.views import (
    StatesAndCities,
    Cities,
    States,
)

# .../<int:id>/ is declaring that there will be an integer
# that will be named 'id' in the view function, that is
# required
urlpatterns = [
    path('', StatesAndCities.as_view(), name='states_and_cities'),
    path('cities/', Cities.CitiesList.as_view(), name='cities'),
    path('cities/details/<int:city_id>/', Cities.CityDetails.as_view(), name='detailed_cities'),
    path('cities/create/', Cities.CityCreate.as_view(), name='create_city'),
    path('cities/delete/<int:pk>', Cities.CityDelete.as_view(), name='delete_city'),
    path('cities/update/<int:pk>', Cities.CityUpdate.as_view(), name='update_city'),
    path('states/', States.ListStates.as_view(), name='states'),
    path('states/details/<int:pk>', States.StateDetails.as_view(), name='details_state'),
    path('states/create/', States.StateCreate.as_view(), name='create_state'),
    path('states/delete/<int:pk>', States.StateDelete.as_view(), name='delete_state'),
    path('states/update/<int:pk>', States.StateUpdate.as_view(), name='update_state'),
]
