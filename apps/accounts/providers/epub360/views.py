import logging
import json

import requests
from allauth.socialaccount.providers.oauth.client import OAuth
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import Epub360Provider

logger = logging.getLogger("django")


class Epub360API(OAuth):
    url = "http://www.epub360.com/oauth2/me"

    def get_user_info(self):
        data = json.loads(self.query(self.url))
        logger.info(data)
        return data["response"]["user"]


class Epub360OAuthAdapter(OAuth2Adapter):
    provider_id = Epub360Provider.id
    access_token_url = "http://www.epub360.com/oauth2/access_token"
    authorize_url = "http://www.epub360.com/oauth2/authorize"
    profile_url = "http://www.epub360.com/oauth2/me"
    access_token_method = "GET"

    def complete_login(self, request, app, token, response):
        params = {"access_token": token.token}
        resp = requests.get(self.profile_url, params=params)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)

    def get_callback_url(self, request, app):
        return "http://dash.21epub.com/login/epub360/callback/"


oauth_login = OAuth2LoginView.adapter_view(Epub360OAuthAdapter)
oauth_callback = OAuth2CallbackView.adapter_view(Epub360OAuthAdapter)
