from rest_framework import serializers
from login.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'password',
									'otp',
									'contact',
									'email_id',
									'status')