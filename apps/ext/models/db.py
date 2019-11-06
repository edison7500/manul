from django.db import models
from django.utils import timezone


class BaseModel(models.Model):

    created = models.DateTimeField(default=timezone.now(), editable=False, db_index=True)
    updated = models.DateTimeField(auto_now=True, editable=False, db_index=True)

    class Meta:
        abstract = True