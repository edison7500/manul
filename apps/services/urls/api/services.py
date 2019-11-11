from django.urls import path
from apps.services.views.api import ServiceListAPIView, ServiceDetailAPIView

app_name = "services"
urlpatterns = [
    path("", ServiceListAPIView.as_view(), name="index"),
    path("<int:pk>/", ServiceDetailAPIView.as_view(), name="detail"),
    path("<int:pk>/verify/", ServiceDetailAPIView.as_view(), name="detail")
]
