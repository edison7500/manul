from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^accounts/', include('allauth.urls')),
]

urlpatterns += [path("api/", include("manul.urls.api"))]
