# CIDC Training

Tracking progress of videos

[X] Video 1

[X] Video 2

[X] Video 3

[X] Video 4

[X] Video 5

[] Video 6

[] Video 7

[] Video 8

[] Video 9

[] Video 10

[] Video 11


## Django tips
### Activities
* Add the following features for States:

[X] Model

[X] views 

[X] create 

[X] delete

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