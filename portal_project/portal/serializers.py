from rest_framework import serializers
from django.db import models
from .models import SchoolGroup, ClassGroup, PostModels, ChatSpace
from user_profile.models import UserProfile, UserAvatar
from accounts.models import UserAccount
from user_profile.serializers import UserProfileSerializer, UserAvatarSerializer
from djoser.serializers import UserCreateSerializer


class SchoolGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolGroup
        fields = "__all__"


class ClassSchoolSerialier(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = "__all__"


class PostModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModels
        fields = [
            "id",
            "title",
            "content",
            "created",
            "poster",
        ]


class PosterInfomationSerializer(serializers.ModelSerializer):
    fullname_set = serializers.CharField(read_only=True, source="user_profile.fullname")
    avatar_set = serializers.ImageField(max_length=255, source="user_avatar.avatar")
    user_id = serializers.IntegerField(source="id")

    class Meta:
        model = UserAccount
        fields = [
            "user_id",
            "fullname_set",
            "avatar_set",
        ]

class ChatSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSpace
        fields = "__all__"
