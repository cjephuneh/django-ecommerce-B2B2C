"""
Django settings for main project.
Generated by 'django-admin startproject' using Django 3.1.5.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from distutils.command.build import build
from operator import truediv
from pathlib import Path
import os
import mimetypes

mimetypes.add_type("text/javascript", ".js", True)
mimetypes.add_type("text/css", ".css", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dr&-v@o7w9#&#r3wj$d#$t78t&*hb$&(2)xa5@05d1p$)1=$96'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', ]

STRIPE_PUB_KEY = 'pk_test_51Ikdb4HwFojfx57irEolkyNAWZCsGCRlrBEKIt4WZXhOTg25Lw50WpUFY5OmDb504spl1XcnaQlswKQu0ULBkpbD003XV2jNJt'
STRIPE_SECRET_KEY = 'sk_test_51Ikdb4HwFojfx57ik70ouFvnOA2MWIE2QqZkcCmB3yO142YvuuLWc4pSBkI5yDT4y77a9oDq6NWWYXxNtGn52A3700yNZd411N'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'vendor_admin'
LOGOUT_REDIRECT_URL = 'frontpage'

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'
COUPON_SESSION_ID = 'coupon'
SESSION_SAVE_EVERY_REQUEST = True


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'djrichtextfield',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    # 'django_markdown',
    'ckeditor',
    'ckeditor_uploader',

    'apps.cart',
    'apps.core',
    'apps.newsletter',
    'apps.order',
    'apps.product',
    'apps.vendor',
    'apps.blog',
    'apps.coupon',
    'apps.newProduct',
    'apps.home',
    'apps.transporter',
    'apps.ordering',
    'apps.maintenance',
    'apps.rental',
    'apps.services',


    # 'rest_framework',
    'widget_tweaks',
    'crispy_forms',
    'mathfilters',
    'bootstrap4',
    'django_addanother',
    'django_select2',
    "compressor",
    'storages',
    "collectfast",
    'django_ses',
    'taggit',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.maintenance.middleware.UnderConstructionMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]


ROOT_URLCONF = 'main.urls'

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
                'apps.product.context_processors.menu_categories',
                'apps.product.context_processors.rental_categories',
                'apps.product.context_processors.services',
                'apps.cart.context_processors.cart',
                'apps.cart.context_processors.comparing',
            ],
        },
    },
]

UNDER_CONSTRUCTION = False

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


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
# LANGUAGE_CODE = 'fr'
# LANGUAGE_CODE = 'rw'

LANGUAGES = [
    ('en','English'),
    ('fr','French'),
    ('rw','Kinyarwanda')
]

TIME_ZONE = 'Africa/Kigali'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOCALE_PATHS = [
    os.path.join(BASE_DIR,'locale')
]

USE_THOUSAND_SEPARATOR = True
SESSION_SAVE_EVERY_REQUEST = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


EMAIL_BACKEND = 'django_ses.SESBackend'
DEFAULT_EMAIL_FROM = 'customerservice@sokopark.com'
SERVER_EMAIL = 'customerservice@sokopark.com'

AWS_SES_REGION_NAME = 'eu-west-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'


AWS_ACCESS_KEY_ID = 'AKIA2K3OSTWJYNYQ6Q5W'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sokopark'
AWS_S3_REGION_NAME = 'af-south-1'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.af-south-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_PRELOAD_METADATA = True
AWS_DEFAULT_ACL = None
AWS_S3_SECURE_URLS = True
AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age={}, s-maxage={}, must-revalidate'.format(AWS_EXPIRY, AWS_EXPIRY)
}
AWS_LOCATION = 'static'
AWS_IS_GZIPPED = True
COLLECTFAST_THREADS = 20

EMAIL_BACKEND = 'django_ses.SESBackend'
DEFAULT_EMAIL_FROM = 'customerservice@sokopark.com'
SERVER_EMAIL = 'customerservice@sokopark.com'

AWS_SES_REGION_NAME = 'eu-west-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'


AWS_ACCESS_KEY_ID = 'AKIA2K3OSTWJYNYQ6Q5W'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sokopark'
AWS_S3_REGION_NAME = 'af-south-1'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.af-south-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_PRELOAD_METADATA = True
AWS_DEFAULT_ACL = None
AWS_S3_SECURE_URLS = True
AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age={}, s-maxage={}, must-revalidate'.format(AWS_EXPIRY, AWS_EXPIRY)
}
AWS_LOCATION = 'static'
AWS_IS_GZIPPED = True
COLLECTFAST_THREADS = 20

COMPRESS_ROOT = os.path.join(BASE_DIR, "static")
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if not DEBUG:
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'main.s3utils.MediaS3Boto3Storage'
    STATICFILES_STORAGE = 'main.s3utils.CachedS3Boto3Storage'
    COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
    COMPRESS_STORAGE = STATICFILES_STORAGE
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    COMPRESS_URL = STATIC_URL
    
else:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'


# STATIC_ROOT = "/home/ubuntu/static/"
COMPRESS_ENABLED = True
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = False


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

GZIP_CONTENT_TYPES = (
    'text/css',
    'application/javascript',
    'application/x-javascript',
    'text/javascript'
)


CKEDITOR_UPLOAD_PATH = 'images/'
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"


# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
