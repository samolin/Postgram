from rest_framework import serializers

from core.user.models import User
from core.user.serializers import UserSerializer


class RegisterSerializer(UserSerializer):
    """Registration serializer for requsts and user creation."""

    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
