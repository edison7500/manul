from rest_framework import serializers


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

#
# class PerformViewMethodMixin(object):
#
#     def get_view_method(self, method_name):
#         if "view" in self.context:
#             _view = self.context["view"]
#             # if hasattr(_view, method_name):
#             perform_method = getattr(_view, method_name)
#             return perform_method
#         else:
#             raise serializers.ValidationError("can not get view method")
#
#     def perform_method(self, method_name, **kwargs):
#         _method = self.get_view_method(method_name)
#         return _method(**kwargs)
