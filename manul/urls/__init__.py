from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("allauth.urls")),
]

urlpatterns += [path("api/", include("manul.urls.api"))]
