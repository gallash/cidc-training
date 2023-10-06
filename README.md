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


### JINJA2
Do not forget that you can work with Python variables and even add conditionals and loops:
* {% if <condition> %} <statement> {% endif %}  -- it also works with for loop
* {{ object.variable }} -- the 'object' is a key declared inside the 'context' that is passed to the template.
We can also use the 'request's variables.

We can also work with extending the base HTML. Just create a block in the HTML that is meant to be the base HTML,
and extend it with the app's templates.