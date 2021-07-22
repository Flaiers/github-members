from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r(bnyw1h&-&(k$6p(1_m)rzvi&(7cphs-vcpiwktikg6d&ijg5'


# Application definition

INSTALLED_APPS = [
    'DataBaseSync.apps.DatabasesyncConfig'
]


# # Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TIME_ZONE = 'Europe/Moscow'
