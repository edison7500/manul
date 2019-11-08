from .base import *


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3")
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
