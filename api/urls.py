from django.urls import path, include
from rest_framework import routers
from . import views
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'addressbook', AddressBookViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('address/', views.AddressBookViewSet.as_view(), name='address_book'),
    path('address/<int:pk>', views.AddressBookViewSet.as_view(), name='address_book'),
]