from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from addressbook.models import Province
# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class AddressBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = ['id']