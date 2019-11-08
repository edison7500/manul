from .base import *
import os


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL")
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
