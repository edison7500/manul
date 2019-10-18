from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path("services/", include("apps.services.urls.api")),
]


urlpatterns = format_suffix_patterns(urlpatterns)


