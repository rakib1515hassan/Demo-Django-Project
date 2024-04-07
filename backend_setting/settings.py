import os
from pathlib import Path

from datetime import timedelta
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-*k7p1uq7=_=^&k-)l7!raxoxq*(vh+qrdkb1j1qjjb9fc=u(2$'
SECRET_KEY = config('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)



ALLOWED_HOSTS = ['*']

# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_ALL_ORIGINS = True




## For Custom Apps Creat (apps/my_apps )
CUSTOM_APPS = [
    'apps.core.apps.CoreConfig',
    'apps.student.apps.StudentConfig',
]


## For Third Party Apps
THIRD_PARTY_APPS = [

    ## Cleaning Delete Files from Storage
    'django_cleanup.apps.CleanupConfig',

    ## For Ckeditor
    # 'ckeditor', 
    # 'ckeditor_uploader',
]



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

] + CUSTOM_APPS + THIRD_PARTY_APPS




## For Custom User Model
# AUTH_USER_MODEL = 'users.User'
# swappable = 'AUTH_USER_MODEL'




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_setting.urls'




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'apps/dashboards/templates'),
        ],
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



WSGI_APPLICATION = 'backend_setting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": config('DB_NAME'),
#         "USER": config('DB_USER'),
#         "PASSWORD": config('DB_PASSWORD'),
#         "HOST": config('DB_HOST'),
#         "PORT": config('DB_PORT'),

#     }
# }




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")



REMEMBER_ME_EXPIRY = 60 * 60 * 24 * 30  # 30 days in seconds

OTP_TIMEOUT = 3  ## OTP timeout set 3 minutes



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



## Email Configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST = config('EMAIL_HOST', default='localhost')
# EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)

# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')


## SMS Service Configuration (Message Send)
# SMS_PROVIDER = config('SMS_PROVIDER', default='')
# TWILIO_ACCOUNT_SID  = config('TWILIO_ACCOUNT_SID', default='')
# TWILIO_AUTH_TOKEN   = config('TWILIO_AUTH_TOKEN', default='')
# TWILIO_PHONE_NUMBER = config('TWILIO_PHONE_NUMBER', default='')


## AWS S3 Configuration
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# AWS_S3_SIGNATURE_VERSION = "s3v4"
# AWS_S3_FILE_OVERWRITE = True

# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')
# AWS_S3_REGION_NAME   = config('AWS_S3_REGION_NAME', default='')
# AWS_S3_ENDPOINT_URL  = config('AWS_S3_ENDPOINT_URL', default='')
# AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN', default='')





## Social Login 

# GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID', default='')
# GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET', default='')

# FACEBOOK_CLIENT_ID = config('FACEBOOK_CLIENT_ID', default='')
# FACEBOOK_CLIENT_SECRET = config('FACEBOOK_CLIENT_SECRET', default='')

# INSTAGRAM_CLIENT_ID = config('INSTAGRAM_CLIENT_ID', default='')
# INSTAGRAM_CLIENT_SECRET = config('INSTAGRAM_CLIENT_SECRET', default='')
