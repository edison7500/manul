import environ

ROOT_DIR = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env()
env.read_env(str(ROOT_DIR.path(".env")))

DEBUG = env("DJANGO_DEBUG", default=True)  # False if not in os.environ

SECRET_KEY = env("SECRET_KEY", default="only dev replace me")

ALLOWED_HOSTS = ["*"]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL", default=str(ROOT_DIR.path("db.sqlite3")))
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Internationalization
# -------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/topics/i18n/
TIME_ZONE = "Asia/Shanghai"

LANGUAGE_CODE = "zh-hans"

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_X_FORWARDED_HOST = True

SITE_ID = 1

ROOT_URLCONF = "manul.urls"

WSGI_APPLICATION = "manul.wsgi.application"

# Application definition
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.sites",
]

THIRD_PARTY_APPS = ["django_extensions"]

REST_FRAMEWORK_APPS = [
    "rest_framework",
    "drf_yasg",
]

LOCALE_APPS = [
    "apps.services",
]

INSTALLED_APPS = DJANGO_APPS + REST_FRAMEWORK_APPS + THIRD_PARTY_APPS + LOCALE_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Static files (CSS, JavaScript, Images)
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = "/static/"

# REST FRAMEWORK
# ------------------------------------------------------------------------------
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
}

# logging
# ----------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/topics/logging/
from .manul_logging import LOGGING as loggin_config

LOGGING = loggin_config
