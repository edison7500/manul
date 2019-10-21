from django.urls import path
from apps.services.views.api import ServiceTypeListAPIView

app_name = "types"
urlpatterns = [path("", ServiceTypeListAPIView.as_view(), name="index")]
