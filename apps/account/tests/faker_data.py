import factory
from faker import Faker
from django.contrib.auth import get_user_model
# from rest_framework.permissions import IsAuthenticated

f = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('username',)

    username = f.user_name()
