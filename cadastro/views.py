from django.shortcuts import render, get_object_or_404, redirect
from cadastro.models import Cidade
from cadastro.forms import CidadeForm


# Create your views here.
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
        'list_cities/list_cities.html',
        context
    )


def detailed_cities_qs(request):
    city = get_object_or_404(Cidade, pk=request.GET['id'])

    return render(
        request,
        template_name='list_cities/detailed_city.html',
        context={'city': city}
    )


def detailed_cities_param(request, city_id):
    city = get_object_or_404(Cidade, pk=city_id)

    return render(
        request,
        template_name='list_cities/detailed_city.html',
        context={'city': city}
    )


def create_city(request):
    if request.method == "POST":
        form = CidadeForm(request.POST)
        # Still lacks, cleaning, checking, checking for duplicates
        if form.is_valid():
            # One of the forms of not allowing duplicates is by putting
            # a True "unique" key in the Model definition
            form.save()
            return redirect(to='list_cities')
    else:
        form = CidadeForm()

    context = {
        'form': form
    }
    return render(
        request,
        template_name='list_cities/creation_form.html',
        context=context
    )


def delete_city(request, city_id):
    city = get_object_or_404(Cidade, pk=city_id)
    city.delete()
    return redirect(to='list_cities')
