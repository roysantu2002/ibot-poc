"""
"""

import os
from datetime import timedelta
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')
print(SECRET_KEY)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', True)
if DEBUG in ['OFF', 'off', 'No', 'no', 'False', 'false', '0', '']:
    DEBUG = False
else:
    DEBUG = True
print(DEBUG)
# ALLOWED_HOSTS = ['auth-core-app.herokuapp.com', 'localhost', '127.0.0.1']
# ALLOWED_HOSTS = ['auth-core-app.herokuapp.com', '127.0.0.1', 'localhost', '0.0.0.0']

"""
ALLOWED_HOSTS
"""

ENV_ALLOWED_HOST = os.environ.get("ALLOWED_HOSTS").split(" ")
ALLOWED_HOSTS = []

if ENV_ALLOWED_HOST:
    ALLOWED_HOSTS = ENV_ALLOWED_HOST

print(ALLOWED_HOSTS)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'api',
    'accounts',
    'ldnsql',
    'ldnservers',
    'rest_framework',
    # 'rest_framework.authtoken',
    'drf_spectacular',
    # 'drf-yasg',
    'rest_framework_simplejwt.token_blacklist',
    'django_extensions',
    'corsheaders'


]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# mongoengine.connect(db='coreapp', host='127.0.0.1', username=username, password=pwd)

if os.environ.get('DJANGO_DEBUG') == 1:
    DATABASES = dj_database_url.config(conn_max_age=600, ssl_require=True)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.environ.get('DB_HOST'),
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASS'),
        }
    }

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         },
#         "KEY_PREFIX": "example"
#     }
# }
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379
#
# # Cache time to live is 15 minutes.
# CACHE_TTL = 60 * 15


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
     'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #  'rest_framework.permissions.AllowAny',
         'rest_framework_simplejwt.authentication.JWTAuthentication',
       'rest_framework.authentication.SessionAuthentication',
    #    'rest_framework.authentication.TokenAuthentication',
       'rest_framework.authentication.BasicAuthentication',
   ),
    'DEFAULT_PERMISSION_CLASSES': [
          'rest_framework.permissions.IsAuthenticated',
          'rest_framework.permissions.AllowAny',

    ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.AllowAny',
    # ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # )
}

SPECTACULAR_SETTINGS = {
    'COMPONENT_SPLIT_REQUEST': True,
    'TITLE': 'ibots api',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
}
# permission:
# AllowAny
# IsAuthenticated
# IsAdminUser
# IsAuthenticatedOrReadOnly

CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:3000', 'http://localhost:8000', 'http://0.0.0.0:8000']
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


"""
static url
"""
STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
#
# STATIC_URL = '/static/'
# # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_TMP = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    # 'USER_ID_FIELD': 'email',
    # 'USER_ID_CLAIM': 'email',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Custom user model
AUTH_USER_MODEL = "accounts.User"

# REST_FRAMEWORK = {
#     'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
# }

SPECTACULAR_SETTINGS = {
    'COMPONENT_SPLIT_REQUEST': True,
}

"""
LOGGER
"""
LOGGING = {
    'version': 1,
    # The version number of our log
    'disable_existing_loggers': False,
    'formatters' :{
        'verbose': {
            'format' : '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
             'format' : '%(levelname)s %(asctime)s %(module)s %(funcName)s %(lineno)d %(message)s'
        },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    },
    # django uses some of its own loggers for internal operations. In case you want to disable them just replace the False above with true.
    # A handler for WARNING. It is basically writing the WARNING messages into a file called WARNING.log
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'inf': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'info.log'),
            # 'maxBytes': 300*1024*1024,
            # 'backupCount': 10,
            'formatter': 'verbose',
            # 'encoding': 'uft-8',
        },
        'demo': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'demo.log'),
            # 'maxBytes': 300*1024*50,
            # 'backupCount': 5,
            'formatter': 'verbose',
            # 'encoding': 'uft-8'
        },
        'ibots': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'ibots.log'),
            # 'maxBytes': 1024*1024*1000, # 1000 MB
            # 'backupCount': 5,
            'formatter': 'verbose',
            # 'encoding': 'uft-8'
        }
    },
    # A logger for WARNING which has a handler called 'file'. A logger can have multiple handler
    'loggers': {
       # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
        'django': {
            'handlers': ['console', 'inf'], #notice how file variable is called in handler which has been defined above
            'level': 'INFO',
            'propagate': True,
        },
        'demo_log':{
             'handlers': ['demo'], #notice how file variable is called in handler which has been defined above
            'level': 'INFO',
            'propagate': True,
        },
        'ibots_log':{
            'handlers': ['ibots'], #notice how file variable is called in handler which has been defined above
            'level': 'INFO',
            'propagate': True,
        }
    },
}