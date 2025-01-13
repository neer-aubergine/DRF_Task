from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'image',
            'bio',
            'phone',
        )
        extra_kwargs = {'password': {'write_only': True}}