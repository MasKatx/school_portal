from rest_framework import serializers
from .models import SchoolGroup, ClassGroup


class SchoolGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolGroup
        fields = "__all__"


class ClassSchoolSerialier(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = "__all__"
