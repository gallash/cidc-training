from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "inatel",
        'USER': "postgres",
        'PASSWORD': "root",
        'HOST': "127.0.0.1",
        'PORT': "5433"
    }
}

AUTH_PASSWORD_VALIDATORS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
