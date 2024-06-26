

from pathlib import Path
import os
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


TEMPLATES_DIR=os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')
MEDIA_DIR=os.path.join(BASE_DIR,'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = "django-insecure-5dj)a6x=-s@yv@^-%62@p#d*cv#g46yxeuw*(ky-1bh0dtad1f"
SECRET_KEY=config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['a08a-103-189-158-202.ngrok-free.app']
# CSRF_TRUSTED_ORIGINS = ['https://a08a-103-189-158-202.ngrok-free.app']
ALLOWED_HOSTS = []




# Application definition

INSTALLED_APPS = [
    'daphne',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'user_auth',
    'products',
    'product_categories',
    'cart',
    'orders',
    'payments',
    'admin_panel',
    'system_setting',
    'chat_notification',
    'custom_middleware'
    
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
]

ROOT_URLCONF = "ecommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR,],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "product_categories.views.category_context_processors.categories",
                "product_categories.views.brand_context_processor.brands",
                "system_setting.views.contact_and_details.contact_and_details", 
                "chat_notification.context_processor.notification_context_processor",  
            ],
            'libraries':{
            'cart_tag': 'cart.templatetags.cart_tag',
            
            
            }
        },
    },
]

#WSGI_APPLICATION = "ecommerce.wsgi.application"
ASGI_APPLICATION = "ecommerce.asgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': "channels.layers.InMemoryChannelLayer"
    }
}


AUTH_USER_MODEL= 'user_auth.User'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[STATIC_DIR,]

#Media
MEDIA_URL='/media/'
MEDIA_ROOT=MEDIA_DIR

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# Email Configuration

EMAIL_HOST=config('EMAIL_HOST')
EMAIL_PORT=config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True


AUTHENTICATION_BACKENDS = [
    'user_auth.views.authentication.custom_authentication.CustomAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',

]
