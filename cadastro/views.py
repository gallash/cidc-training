from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from cadastro.models import Cidade, State, Country
from cadastro.forms import CidadeForm, StateForm, CountryForm


# Main view
class StatesAndCities(TemplateView):
    """
    TemplateView renders a template. Can send additional information as well
    by overriding the 'get_context_data' method
    """
    template_name = 'countries_states_and_cities/countries_states_and_cities.html'


class Cities:
    class CitiesList(ListView):
        # Name of the object passed in the context dictionary
        context_object_name = 'cities'
        queryset = Cidade.objects.all().order_by('nome')
        template_name = 'cities/list.html'

    class CityDetails(DetailView):
        # model receives the main context data.
        model = Cidade
        context_object_name = 'city'  # Defines the name of the context object
        pk_url_kwarg = 'city_id'  # Changes the expected 'pk' to 'city_id'
        template_name = 'cities/details.html'

        def get_context_data(self, **kwargs):
            # In the get_context_data function, we define the additional data to
            # be passed
            context = super().get_context_data(**kwargs)
            context['city_name'] = self.object.nome
            return context

    class CityCreate(CreateView, SuccessMessageMixin):
        model = Cidade
        form_class = CidadeForm
        template_name = 'cities/creation_form.html'

        success_url = reverse_lazy('cities')

    class CityDelete(DeleteView):
        model = Cidade
        context_object_name = 'city'
        template_name = 'cities/deletion_form.html'
        success_url = reverse_lazy('cities')

    class CityUpdate(UpdateView):
        model = Cidade
        form_class = CidadeForm
        template_name = 'cities/update_form.html'
        success_url = reverse_lazy('cities')

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['pk'] = self.object.pk
            return context


class States:
    class StatesList(ListView):
        """
        ListView can display either from model or from querysets
        """
        queryset = State.objects.all().order_by('name')
        context_object_name = 'states'
        template_name = 'states/list.html'

    class StateDetails(DetailView):
        """
        DetailView will automatically expect receiving the 'pk'
        for searching in the database for the specific entry
        and then displaying it. Alter the name of the variable
        for 'pk' to something else if necessary, by modifying
        'pk_url_kwarg'
        """
        model = State
        context_object_name = 'state'
        template_name = 'states/details.html'

    class StateCreate(CreateView):
        model = State
        form_class = StateForm
        template_name = 'states/creation_form.html'
        success_url = reverse_lazy('states')

    class StateUpdate(UpdateView):
        model = State
        form_class = StateForm
        template_name = 'states/update_form.html'
        success_url = reverse_lazy('states')

    class StateDelete(DeleteView):
        model = State
        template_name = 'states/deletion_form.html'
        success_url = reverse_lazy('states')

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['state_name'] = self.object.name
            return context


class Countries:
    class CountriesList(ListView):
        """
        ListView can display either from model or from querysets
        """
        queryset = Country.objects.all().order_by('name')
        context_object_name = 'countries'
        template_name = 'countries/list.html'

    class CountriesDetails(DetailView):
        """
        DetailView will automatically expect receiving the 'pk'
        for searching in the database for the specific entry
        and then displaying it. Alter the name of the variable
        for 'pk' to something else if necessary, by modifying
        'pk_url_kwarg'
        """
        model = Country
        context_object_name = 'country'
        template_name = 'countries/details.html'

    class CountriesCreate(CreateView):
        model = Country
        form_class = CountryForm
        template_name = 'countries/creation_form.html'
        success_url = reverse_lazy('countries')

    class CountriesUpdate(UpdateView):
        model = Country
        form_class = StateForm
        template_name = 'countries/update_form.html'
        success_url = reverse_lazy('countries')

    class CountriesDelete(DeleteView):
        model = Country
        template_name = 'countries/deletion_form.html'
        success_url = reverse_lazy('countries')

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['country_name'] = self.object.name
            return context
