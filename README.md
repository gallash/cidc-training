# CIDC Training

Tracking progress of videos

[X] Video 1

[X] Video 2

[X] Video 3

[X] Video 4

[X] Video 5

[X] Video 6

[X] Video 7

[] Video 8

[] Video 9

[] Video 10

[] Video 11


## Docker
### Configuring Docker
* Docker Compose
Containerize multiple

* Dockerfile

* Environments separation: development and production


## Django tips

### Activities
* Add CRUD for States and Countries:

[X] States

[X] Countries


### Function based and Class based Views
There are things that are very specific. These very specific functionalities can be built in a function
or using inheriting from the View class.

There are also generic classes (ViewList) that abstract from Detail page, Create Page, etc. These I can
take advantage from generic classes already implemented in Django. There is also a website called 
[CCBV](https://ccbv.co.uk/) which serves as a great compiler of Django class based view information.

[Django Course](https://www.youtube.com/playlist?list=PLj7fuoRtNDcelpc_sTM_dwh6QUwrahUNj)

Now I am changing form List and Detail views from function based views to Class based views.


### JINJA2
Do not forget that you can work with Python variables and even add conditionals and loops:
* {% if <condition> %} <statement> {% endif %}  -- it also works with for loop
* {{ object.variable }} -- the 'object' is a key declared inside the 'context' that is passed to the template.
We can also use the 'request's variables.

We can also work with extending the base HTML. Just create a block in the HTML that is meant to be the base HTML,
and extend it with the app's templates.

### Configure and Run Django in Production
[Read this](https://marketsplash.com/tutorials/django/how-to-run-django-in-production/#:~:text=Django's%20static%20and%20media%20files,them%20using%20Django's%20collectstatic%20command.&text=Run%20the%20collectstatic%20command%20to,files%20into%20the%20STATIC_ROOT%20directory.)
 for more information on how we can configure a secure and optimal Django environment server opened to other computers

Remember that [python manage.py is meant for development](https://stackoverflow.com/questions/61157573/manage-py-runserver-is-frequently-reloading-in-production). 
The necessary steps for configuring the WSGI can be found [here](https://stackoverflow.com/questions/69659258/do-we-need-to-use-runserver-command-in-production-to-start-our-django-project). 
Read the WSGI documentation for more details [here](https://uwsgi-docs.readthedocs.io/en/latest/). 

[Read this](https://vsupalov.com/django-runserver-in-production/) for more information on why it is necessary to 
configure Nginx and Gunicorn to run with Django in production.

[Read this](https://vsupalov.com/gunicorn-and-nginx/) to further understand the relationship between Nginx and Gunicorn.