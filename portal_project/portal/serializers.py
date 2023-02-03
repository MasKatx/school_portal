from rest_framework import serializers
from .models import SchoolGroup, ClassGroup, PostModels, ChatSpace


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
        fields = "__all__"

class ChatSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSpace
        fields = "__all__"
