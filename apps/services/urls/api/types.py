from django.urls import path
from apps.services.views.api import ServiceTypeListAPIView, ServiceTypeDetailAPIView

app_name = "types"
urlpatterns = [
    path("", ServiceTypeListAPIView.as_view(), name="index"),
    path("<int:pk>/", ServiceTypeDetailAPIView.as_view(), name="detail"),
]
