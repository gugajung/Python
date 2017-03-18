# -*- coding: utf-8 -*-
import django
import os
# Django settings for sincomercio project.

DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
                
#                CONEXAO SYS
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sincomercio', # Or path to database file if using sqlite3.
        'USER': 'sysnetwork', # Not used with sqlite3.
        'PASSWORD': 'sysnet8662BD', # Not used with sqlite3.
        'HOST': '201.28.115.228', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.

#            CONEXAO LOCAL
#       'NAME': 'sincomercio', # Or path to database file if using sqlite3.
#       'USER': 'root', # Not used with sqlite3.
#       'PASSWORD': '', # Not used with sqlite3.
#       'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
#       'PORT': '', # Set to empty string for default. Not used with sqlite3.

#            CONEXAO SINCOMERCIO
#       'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#      'NAME': 'sincomercio', # Or path to database file if using sqlite3.
#      'USER':'sincomercio',
#      'PASSWORD':'sincomercio8662BD',
#      'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

## Raiz do django
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))

## Raiz da aplica��o
APP_ROOT = os.path.dirname(os.path.realpath(__file__))

## Caminho relativo do diretorio de medias, a partir da raiz do projeto
MEDIA_RELATIVE_PATH = 'midias' 

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(APP_ROOT, MEDIA_RELATIVE_PATH)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"

#MEDIA_URL = '/testes/django/sincomercio/midias/'
MEDIA_URL = '/midias/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/midias/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3w633u@qfuwwbww8_vfl2xn4tb*m2=hgn&m!o3mt)0-k-e5b-n'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)
LOGIN_REDIRECT_URL ="/admin/"
ROOT_URLCONF = 'sincomercio.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(APP_ROOT, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'sincomercio.noticias',
    'sincomercio.videoteca',
    'sincomercio.campanhas',
    'sincomercio.imagens',
    'sincomercio.acoes_sociais',
    'sincomercio.loja_aniver',
    'sincomercio.banners',
    'sincomercio.links',
    'sincomercio.associados',
    'sincomercio.comunicados',
    'sincomercio.arquivos',
    'sincomercio.contribuicoes',
    'sincomercio.parceiros',
    'sincomercio.eventos',
	'sincomercio.palestras',
    'sorl.thumbnail',
    'pagination',
    'sincomercio.calendario',
    'sincomercio.calendarioMercado'
)

# CONFIGURACOES DO SERVIDOR DE EMAIL
EMAIL_HOST = 'smtp.sysnetwork.com.br'
EMAIL_HOST_USER = 'noc@sysnetwork.com.br'
EMAIL_HOST_PASSWORD = 'adm2010sys'
EMAIL_SUBJECT_PREFIX = '[SinComercio Matao]'
EMAIL_PORT = 25
EMAIL_USE_TLS = True


FILE_UPLOAD_MAX_MEMORY_SIZE = 47185920 # 45 MB
