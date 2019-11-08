from .base import *
import os


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db(os.environ.get(
        "DATABASE_URL",
        str(ROOT_DIR.path("db.sqlite3")))
    )
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
