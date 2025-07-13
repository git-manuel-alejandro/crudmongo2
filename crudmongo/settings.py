from pathlib import Path
from mongoengine import connect

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-testkey'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'productos',
]

MIDDLEWARE = []

ROOT_URLCONF = 'crudmongo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]

WSGI_APPLICATION = 'crudmongo.wsgi.application'

connect(
    db="crudmongo_db", 
    host="localhost", 
    port=27017
)
