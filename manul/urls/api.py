from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path("types/", include("apps.services.urls.api.types")),
    path("services/", include("apps.services.urls.api.services")),
]


urlpatterns = format_suffix_patterns(urlpatterns)


