from django.urls import path
from apps.services.views.api import ServiceTypeListAPIView, ServiceDetailAPIView

app_name = "types"
urlpatterns = [
    path("", ServiceTypeListAPIView.as_view(), name="index"),
    path("<int:id>/", ServiceDetailAPIView.as_view(), name="detail"),
]
