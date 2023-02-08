from rest_framework import serializers
from .models import UserProfile, UserAvatar
from djoser.serializers import UserCreateSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAvatar
        fields = "__all__"


class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"
