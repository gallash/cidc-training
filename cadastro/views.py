from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError

from cadastro.models import Cidade, State
from cadastro.forms import CidadeForm, StateForm


# Create your views here.
# Main view
def states_and_cities(request):
    return render(
        request,
        template_name='states_and_cities/states_and_cities.html',
        context={}
    )


# Cities
def list_cities(request):
    if request.GET.__len__():
        # If I use .get() I will get the object, instead of the
        # QuerySet, and the object is not iterable
        query_set = Cidade.objects.filter(pk=request.GET['id'])
    else:
        query_set = Cidade.objects.all().order_by('nome')

    context = {
        "cities": query_set
    }

    # As we are using templates, and we passed the name
    # "templates" to the 'list' parameter in the settings.py
    # file, all subdirectories and files inside the dir
    # 'template' or the app directory will be 'merged' into one
    #
    # Note that we are passing both 'request' and 'context' to
    # the HTML template. Therefore, we can use them between
    # curly braces
    return render(
        request,
        'cities/list.html',
        context
    )


def detailed_cities_qs(request):
    city = get_object_or_404(Cidade, pk=request.GET['id'])

    return render(
        request,
        template_name='cities/details.html',
        context={'city': city}
    )


def detailed_cities_param(request, city_id):
    city = get_object_or_404(Cidade, pk=city_id)

    return render(
        request,
        template_name='cities/details.html',
        context={'city': city}
    )


def create_city(request):
    errors = ""
    if request.method == "POST":
        form = CidadeForm(request.POST)
        # Still lacks, cleaning, checking, checking for duplicates
        try:
            if form.is_valid():
                # One of the forms of not allowing duplicates is by putting
                # a True "unique" key in the Model definition
                form.save()
                return redirect(to='cities')
        except IntegrityError as ie:
            errors = ie
    else:
        form = CidadeForm()

    return render(
        request,
        template_name='cities/creation_form.html',
        context={'form': form, 'errors': errors}
    )


def delete_city(request, city_id):
    city = get_object_or_404(Cidade, pk=city_id)
    city.delete()
    return redirect(to='cities')


def update_city(request, city_id):
    # Receiving the city_id via URL parameter is a little problematic
    # in this case because in the <form> a param will be required
    # all the time. Hence, I would have to pass the additional key-value pair
    # 'city_id' in the context.
    # There is another way for me to do it, which is receiving it via query strings
    city = get_object_or_404(Cidade, pk=city_id)
    if request.method == 'GET':
        form = CidadeForm(instance=city)
    elif request.method == 'POST':
        form = CidadeForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect(to='cities')

    return render(
        request,
        template_name='cities/update_form.html',
        context={'form': form, 'city_id': city_id}
    )


# States
def list_states(request):
    states = State.objects.all().order_by('name')
    return render(
        request,
        template_name='states/list.html',
        context={'states': states}
    )


def detailed_state(request, state_id):
    state = get_object_or_404(State, pk=state_id)
    return render(
        request,
        template_name='states/details.html',
        context={'state': state}
    )


def create_state(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='states')
    else:
        form = StateForm()

    return render(
        request,
        template_name='states/creation_form.html',
        context={'form': form}
    )


def delete_state(request, state_id):
    state = get_object_or_404(State, pk=state_id)
    state.delete()
    return redirect(to='states')
