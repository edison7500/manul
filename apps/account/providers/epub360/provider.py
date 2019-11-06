import logging
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider

logger = logging.getLogger("django")


class Epub360Account(ProviderAccount):
    def get_profile_url(self):
        return 'https://www.epub360.com/' \
               % self.account.extra_data.get('name')

    def to_str(self):
        dflt = super(Epub360Account, self).to_str()
        name = self.account.extra_data.get('name', dflt)
        return name


class Epub360Provider(OAuth2Provider):
    id = 'epub360'
    name = 'epub360'
    account_class = Epub360Account

    def get_default_scope(self):
        scope = ["openid"]
        return scope

    def extract_uid(self, data):
        logger.info(data)
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(username=data.get('username'), )


provider_classes = [Epub360Provider]
