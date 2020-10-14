"""
Django settings for augustasmell project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, environ

# Environment variables
env = environ.Env()
# reading .env file
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="qsrxo-sz)z&d%9j_w!hzi8909bkh7_f3n$d5lmt&!t9=c)9)p1")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=1)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'smell',
    'profanity',
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'augustasmell.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'augustasmell.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env("ENGINE", default='django.db.backends.sqlite3'),
        'NAME': env("NAME", default=os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': env("USER", default=''),
        'PASSWORD': env("PASSWORD", default=''),
        'HOST': env("HOST", default=''),
        'PORT': env("PORT", default=''), 
    }
}

if DATABASES['default']['ENGINE'] == "sql_server.pyodbc":
    DATABASES['default']['OPTIONS'] = {
        'driver': env("DRIVER"),
        'MARS_Connection': 'True',
    }



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# Azure stuff for static files

DEFAULT_FILE_STORAGE = 'augustasmell.custom_storage.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'augustasmell.custom_storage.custom_azure.AzureStaticStorage'

AZURE_ACCOUNT_NAME = env('AZURE_ACCOUNT_NAME', default="")
AZURE_STORAGE_KEY = env('AZURE_STORAGE_KEY', default="")
AZURE_MEDIA_CONTAINER = env('AZURE_MEDIA_CONTAINER', default='media')
AZURE_STATIC_CONTAINER = env('AZURE_STATIC_CONTAINER', default='static')

# Files URL
#AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.azureedge.net'  # CDN URL
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

