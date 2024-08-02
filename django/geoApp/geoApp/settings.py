"""
Django settings for geoApp project.

Generated by 'django-admin startproject' using Django 3.1.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g*poy*r@6$ixpm9vt&wd_sz7ve(^=+ko*uluydci=l9vl5@!t-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shp',
    'tiff'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', #zips up static files
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'geoApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        # done in the course
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'geoApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# here i am defining that a database named geoapp is created on a server service of postgres crated on localhost, 
# with postgres running on port 5432 (can be switched by postgres configs)
# and that server is uned username postgres and the password for postgres user is 'password'
# this can b changed in postgres shell (sudo -i -u postgres; psql)
# with command 
# ALTER USER postgres WITH PASSWORD 'password';

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # creo il db dalla interfaccia di pgadmin - db: geoappdb -  
        # - va bene anche farlo dalla shell come superuser postgres
        'NAME': 'geoappdb',
        'USER': 'geoapp_main',
        'PASSWORD': 'geomain',  # ALTER USER postgres WITH PASSWORD 'password';
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# psql -d geoappdb -U geoapp_main -h localhost

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# url pattern della cartella in cui risiedono gli static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# where the static files are  copied via collectstatic

# static files = img, css, js
#  li mettero nella cartella static
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'geoApp/static') ]
# where I put my static files

# this is my add
STATICSTORAGE = "Whitenoise.storage.CompressedManifestStaticFilesStorage" #zips up static files

# my adds
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# lets leave media, by following django defaults





