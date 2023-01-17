from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sl546dndh0@_fg63@e5*khvie8)gg5=f@jfdj7$5um)v-vppy6'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '192.168.29.80']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}