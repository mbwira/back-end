from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from addressbook.models import Province, Sector
import account
# Serializers define the API representation.

class AccountProfileSerializer(serializers.ModelSerializer):
	# serialises a citizen profile object
	class Meta:
		model = account.models.Account
		fields = [
			'id',
			'email',
			
		]