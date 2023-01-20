from rest_framework import generics
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user_profile.models import UserProfile

# django
from django.http import JsonResponse

# import models
from .models import SchoolGroup, ClassGroup

# import models serializer
from .serializers import SchoolGroupSerializer, ClassSchoolSerialier


def check_user_type_type(user):
    user_type = UserProfile.objects.get(user=user).user_type
    return user_type


# HANDLE SCHOOL GROUP
class SchoolGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            user = self.request.user
            if check_user_type_type(user) == "1":
                school_group = SchoolGroup.objects.filter(user_id=user.id)
                school_group = SchoolGroupSerializer(school_group, many=True)
                # return JsonResponse({"access": "ok"})
                return JsonResponse(school_group.data, safe=False)
        except:
            return JsonResponse({"value": "error"})


class CreateOrUpdateSchoolGroupView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = self.request.user
        if check_user_type_type(user) == "1":
            data = self.request.data
            group_id = data["group_id"]
            group_id = f"{group_id}".upper()
            group_name = data["group_name"]
            group_phone = data["group_phone"]
            group_address = data["group_address"]
            abbreviation = data["abbreviation"]
            abbreviation = f"{abbreviation}".upper()
            try:
                if request.method == "POST":
                    SchoolGroup.objects.create(
                        group_name=group_name,
                        group_phone=group_phone,
                        group_address=group_address,
                        group_id=group_id,
                        sign=abbreviation,
                        user_id=user.id,
                    )

                    school_group = SchoolGroup.objects.get(
                        group_id=group_id, user_id=user.id
                    )

                    school_group = SchoolGroupSerializer(school_group)
                    return JsonResponse(school_group.data)
                    # return JsonResponse(school_group.data)
            except:
                return JsonResponse(
                    {"error": "its exists before try to orther group id?"}
                )

    def put(self, request, pk, format=None):
        user = self.request.user
        if check_user_type_type(user) == "1":
            data = self.request.data
            group_id = data["group_id"]
            group_id = f"{group_id}".upper()
            group_name = data["group_name"]
            group_phone = data["group_phone"]
            group_address = data["group_address"]
            abbreviation = data["abbreviation"]
            abbreviation = f"{abbreviation}".upper()
            try:
                SchoolGroup.objects.update_or_create(
                    pk=pk,
                    defaults={
                        "group_id": group_id,
                        "group_name": group_name,
                        "group_phone": group_phone,
                        "group_address": group_address,
                        "sign": abbreviation,
                    },
                )
                school_group = SchoolGroup.objects.get(
                    group_id=group_id, user_id=user.id
                )
                school_group = SchoolGroupSerializer(school_group)
                return JsonResponse(school_group.data)
            except:
                return JsonResponse(
                    {"error": "its exists before try to orther group id?"}
                )


class GetDetailSchoolGroup(APIView):
    def get(self, request, format=None):
        user = self.request.user


class DestroySchoolGroupView(APIView):
    serializer_class = SchoolGroupSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = self.request.user
        school_group = SchoolGroup.objects.get(pk=pk, user_id=user.id)
        school_group = SchoolGroupSerializer(school_group)
        return JsonResponse(school_group.data)

    def delete(self, request, pk, format=None):
        user = self.request.user
        if check_user_type_type(user) == "1":
            try:
                school_group = SchoolGroup.objects.get(pk=pk)
                school_group.delete()
                return JsonResponse({"success": "School group be deleted"})
            except:
                return JsonResponse({"error": "u can not deleted this group"})


class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, str, format=None):
        user = self.request.user
        print(str)
        str = f"{str}".upper()
        school_group = SchoolGroup.objects.get(group_id=str)
        school_group_id = school_group.id
        classes_group = ClassGroup.objects.filter(school_group_id=school_group_id)
        classes_group = ClassSchoolSerialier(classes_group, many=True)
        return JsonResponse(classes_group.data, safe=False)


class CreateOrUpdateClassGroupView(APIView):
    permission_classes = [IsAuthenticated]

    # データを取得する
    def get(self, request, format=None):
        class_group = ClassGroup.objects.all()
        class_group = ClassSchoolSerialier(class_group, many=True)
        return JsonResponse(class_group.data, safe=False)

    # クラスグループを作成する
    def post(self, request, format=None):
        data = self.request.data
        user = self.request.user
        print(data)
        class_name = data["class_name"]
        class_student_number = data["class_student_number"]
        class_course = data["class_course"]
        class_manager = data["class_manager"]
        class_submanager = data["class_submanager"]
        group_id = data["group_id"]

        group_id = f"{group_id}".upper()
        group_id = SchoolGroup.objects.get(group_id=group_id)
        ClassGroup.objects.create(
            school_group=group_id,
            class_name=class_name,
            class_studentnumber=class_student_number,
            class_course=class_course,
            class_manager=class_manager,
            class_submanager=class_submanager,
        )

        school_group = SchoolGroup.objects.get(group_id=group_id, user_id=user.id)

        school_group = SchoolGroupSerializer(school_group)
        return JsonResponse(school_group.data)

        # 1,2,3,4,5,6 データを必須

    # クラスデータを
    def put(self, request, pk, format=None):
        user = self.request.user
        if check_user_type_type(user) == "1":
            data = self.request.data
            class_name = data["class_name"]
            class_student_number = data["class_student_number"]
            class_course = data["class_course"]
            class_manager = data["class_manager"]
            class_submanager = data["class_submanager"]
            group_id = data["group_id"]
            group_id = f"{group_id}".upper()
            group_id = SchoolGroup.objects.get(group_id=group_id)
