from allauth.socialaccount.providers.oauth.urls import default_urlpatterns

from .provider import Epub360Provider

urlpatterns = default_urlpatterns(Epub360Provider)
