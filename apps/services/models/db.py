from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
import jsonfield


class ServiceType(models.Model):
    Vendor = Choices((0, "aliyun", _("aliyun")), (1, "tencent", _("tencent")))
    Service = Choices((0, "sms", _("sms")))
    vendor = models.IntegerField(default=Vendor.aliyun, choices=Vendor)
    service = models.IntegerField(default=Service.sms, choices=Service)
    extra = jsonfield.JSONField()

    def __str__(self):
        return "{} - {}".format(self.get_vendor_display(), self.get_service_display())


class Service(models.Model):
    user_id = models.IntegerField(default=0,)
    type = models.ForeignKey("ServiceType", related_name="service_type", on_delete=models.CASCADE)
    app_key = models.CharField(null=False, max_length=255)
    app_secret = models.CharField(null=False, max_length=255)
    title = models.CharField(null=False, max_length=255)
    content = models.TextField(default="", blank=True)

    created_at = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False
    )
    updated_at = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False
    )

    def __str__(self):
        return self.title
