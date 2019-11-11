import jsonfield
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_extensions.db import fields
from model_utils import Choices

# from django_extensions.models im

from django.contrib.auth import get_user_model


class ServiceType(models.Model):
    Vendor = Choices((1, "aliyun", _("aliyun")), (2, "tencent", _("tencent")))
    Service = Choices((1, "sms", _("sms")))
    title = models.CharField(max_length=255)
    vendor = models.IntegerField(default=Vendor.aliyun, choices=Vendor)
    service = models.IntegerField(default=Service.sms, choices=Service)
    options = jsonfield.JSONField()

    class Meta:
        verbose_name = _("service-type")
        verbose_name_plural = _("service-type")

    def __str__(self):
        return "{} - {}".format(self.get_vendor_display(), self.get_service_display())


class Service(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="services", on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        "ServiceType", related_name="service_type", on_delete=models.CASCADE
    )
    app_key = models.CharField(null=False, max_length=255)
    app_secret = models.CharField(null=False, max_length=255)
    title = models.CharField(null=False, max_length=255)
    content = jsonfield.JSONField()

    created_at = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False
    )
    updated_at = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False
    )

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("service")

    def __str__(self):
        return self.title


class SMSVerifyCode(models.Model):
    service = models.ForeignKey(
        Service, related_name="verify_code", on_delete=models.CASCADE
    )
    phone_number = models.CharField(max_length=11)
    code = fields.RandomCharField(
        length=6,
        unique=True,
        lowercase=True,
        include_alpha=False,
        db_index=True,
        editable=False,
    )
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False
    )
    expired_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        unique_together = (("service", "phone_number", "code"),)
        verbose_name = _("sms-verify-code")
        verbose_name_plural = _("sms-verify-code")

    def __str__(self):
        return self.code
