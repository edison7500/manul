from django.db import models
from django.utils import timezone


class Service(models.Model):
    user_id = models.IntegerField()
    vendor = models.IntegerField()
    service = models.IntegerField()
    app_key = models.CharField(null=False, max_length=255)
    app_secret = models.CharField(null=False, max_length=255)
    title = models.CharField(null=False, max_length=255)
    content = models.TextField()

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return self.title
