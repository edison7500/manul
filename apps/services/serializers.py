import json
import logging
import re
from datetime import timedelta, datetime

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from apps.ext.rest.serializers import ProcessCurrentUserMixin
from apps.services.models import ServiceType, Service, SMSVerifyCode

logger = logging.getLogger("django")

phone_number_regex = re.compile(r"^\d{1,11}$", re.IGNORECASE)


def gen_verify_code(service, phone_number, minutes=5) -> str:
    expired_at = datetime.now() + timedelta(minutes=minutes)
    sms_verify_code = SMSVerifyCode.objects.create(
        phone_number=phone_number, service=service, expired_at=expired_at
    )
    return sms_verify_code.code


class ServiceTypeSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField(source="get_vendor_display")
    service = serializers.CharField(source="get_service_display")

    class Meta:
        model = ServiceType
        fields = "__all__"


class ServiceSerializer(ProcessCurrentUserMixin, serializers.ModelSerializer):
    service_type = serializers.SerializerMethodField()

    class Meta:
        model = Service
        exclude = ["user"]
        extra_kwargs = {
            "app_key": {"write_only": True},
            "app_secret": {"write_only": True},
            # "user": {"write_only": True},
            "type": {"write_only": True},
        }

    @swagger_serializer_method(serializer_or_field=serializers.CharField)
    def get_service_type(self, obj):
        return "{} - {}".format(
            obj.type.get_vendor_display(), obj.type.get_service_display()
        )

    def create(self, validated_data):
        service = Service(**validated_data)
        service.user = self.get_current_user()
        service.save()
        return service


class SMSSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        min_length=8, max_length=11, regex=phone_number_regex
    )
    template_param = serializers.JSONField(default={}, required=False)

    def dispatch(self):
        # TODO: SMS Service Route
        pass

    def send_sms(self, service, **kwargs):
        _content = service.content.copy()

        _code = kwargs.get("code", None)
        if _code:
            _tp = {"code": _code}
        else:
            _tp = self.validated_data["template_param"]

        client = AcsClient(service.app_key, service.app_secret)
        req = CommonRequest()
        req.set_accept_format("json")
        req.set_domain("dysmsapi.aliyuncs.com")
        req.set_method("POST")
        req.set_protocol_type("https")  # https | http
        req.set_version("2017-05-25")
        req.set_action_name("SendSms")
        req.add_query_param("RegionId", "cn-hangzhou")
        req.add_query_param("PhoneNumbers", self.validated_data["phone_number"])
        req.add_query_param("SignName", _content["SignName"])
        req.add_query_param("TemplateCode", _content["TemplateCode"])
        req.add_query_param("TemplateParam", json.dumps(_tp))

        res = client.do_action_with_exception(req)
        return json.loads(res)


class SMSVerifiedSerializer(SMSSerializer):
    phone_number = serializers.RegexField(
        min_length=8, max_length=11, regex=phone_number_regex
    )

    def send_sms_with_verifiy(self, service):
        _phone_number = self.validated_data.get("phone_number")
        return self.send_sms(
            service=service, code=gen_verify_code(_phone_number, service)
        )


class SMSVerifiedCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSVerifyCode
        fields = ("code",)
