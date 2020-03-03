# Rest_framework importations
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# django importations
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404
# Other importations
from . import serializers
from addressbook import models
import account



class AccountViewSet(viewsets.ModelViewSet):
     """ Handles creating and updating of Account profiles"""
     serializer_class = serializers.AccountProfileSerializer
     serializer = serializers.AccountProfileSerializer
     queryset = account.models.Account.objects.all()




