from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "inatel",
        'USER': "postgres",
        'PASSWORD': "root",
        'HOST': "inatel_db",  # Points to the instance of the DB that is running in Docker
        'PORT': "5432"  # How do ports work again, how to configure them?
    }
}

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1', 'localhost')
