from django.urls import path
from apps.services.views.api import ServiceListAPIView

app_name = "services"
urlpatterns = [path("", ServiceListAPIView.as_view(), name="index")]
