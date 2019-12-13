from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, AddressBookSerializer
# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressBookViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AddressBookSerializer

# Create your views here.
