class ProcessLanguageMixin(object):
    def get_current_language(self):
        if "request" in self.context:
            _request = self.context["request"]
            _lang = _request.LANGUAGE_CODE
            if _lang == "en":
                _lang = "default"
            return _lang


class ProcessCurrentUserMixin(object):

    def get_current_user(self):
        if "request" in self.context:
            _request = self.context["request"]
            user = _request.user
            return user

