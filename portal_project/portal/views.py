from rest_framework import generics
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user_profile.models import UserProfile

# django
from django.http import JsonResponse

# import models
from .models import SchoolGroup, ClassGroup, PostModels

# import models serializer
from .serializers import (
    SchoolGroupSerializer,
    ClassSchoolSerialier,
    PostModelsSerializer,
)


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
                school_group = school_group.order_by("id")
                school_group = SchoolGroupSerializer(school_group, many=True)
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

                school_group = SchoolGroup.objects.get(id=pk, user_id=user.id)
                profile_belong = UserProfile.objects.filter(
                    teacher_belong_to_name=school_group.group_name,
                    teacher_belong_to_id=school_group.group_id,
                )

                for i in profile_belong:
                    i.teacher_belong_to_name = group_name
                    i.teacher_belong_to_id = group_id
                    i.save()

                SchoolGroup.objects.update_or_create(
                    id=pk,
                    defaults={
                        "group_id": group_id,
                        "group_name": group_name,
                        "group_phone": group_phone,
                        "group_address": group_address,
                        "sign": abbreviation,
                    },
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


# 掲示板の作成
class CreateorUpdatePostView(APIView):
    permission_classes = [IsAuthenticated]

    # データの取得
    def get(self, request, format=None):
        post_models = PostModels.objects.all()
        post_models = PostModelsSerialier(post_models, many=True)
        return JsonResponse(post_models.data, safe=False)

    # 掲示板を作成
    def post(self, request, format=None):
        try:
            data = self.request.data
            user = self.request.user
            post_title = data["post_title"]
            content = data["content"]
            created_by_id = data["created_by_id"]
            group_id = data["group_id"]
            group_id = SchoolGroup.objects.get(group_id=group_id)
            PostModels.objects.create(
                user=group_id,
                title=post_title,
                content=content,
                created_by_id=created_by_id,
            )

            school_post = SchoolGroup.objects.get(group_id=group_id)
            school_post = SchoolGroupSerializer(school_post)

            # return JsonResponse(school_post.data, safe=True)
            return JsonResponse({"success": "Created New Post!"})
        except:
            return JsonResponse({"error": "Not Create New Post..."})

    # 掲示板の更新
    # put --> 更新する
    # 参考になるかもしれないコード
    # portal/views.py(今いるファイル) 204~216行目
    def put(self, request, str, format=None):
        pass


class GetClassSchool(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            user_profile = UserProfile.objects.get(user_id=user.id)
            school_group = SchoolGroup.objects.get(
                group_id=user_profile.teacher_belong_to_id
            )
            class_school = ClassGroup.objects.filter(school_group_id=school_group.id)
            class_school = ClassSchoolSerialier(class_school, many=True)
            return JsonResponse(class_school.data, safe=False)
        except:
            JsonResponse({"error": "somthing wrong right here"})


class CreateClassSchool(APIView):
    def post(self, request, format=None):
        # try:
        user = self.request.user
        data = self.request.data
        class_name = data["class_name"]
        class_course = data["class_course"]
        class_manager = data["class_manager"]
        class_submanager = data["class_submanager"]
        class_studentnumber = data["class_studentnumber"]
        school_group = data["school_group"]
        if check_user_type_type(user) == "2":
            if ClassGroup.objects.filter(class_name=class_name).count() == 0:
                ClassGroup.objects.create(
                    class_name=class_name,
                    class_course=class_course,
                    class_manager=class_manager,
                    class_submanager=class_submanager,
                    class_studentnumber=class_studentnumber,
                    school_group_id=int(school_group),
                )
                return JsonResponse({"success": "created"})
            else:
                return JsonResponse({"error": "・クラス名が既存しました。"})

    # except:
    #     return JsonResponse({"error": "somthing wrong right here"})


class UpdateClassSchool(APIView):
    def put(self, request, pk, format=None):
        # try:
        user = self.request.user
        data = self.request.data
        class_name = data["class_name"]
        class_course = data["class_course"]
        class_manager = data["class_manager"]
        class_submanager = data["class_submanager"]
        class_studentnumber = data["class_studentnumber"]
        if check_user_type_type(user) == "2":
            class_name_check = ClassGroup.objects.get(id=pk).class_name
            print(class_name_check, "check")
            print(class_name)
            if class_name == class_name_check:
                print("ton tai")
                ClassGroup.objects.update_or_create(
                    id=pk,
                    defaults={
                        "class_name": class_name,
                        "class_course": class_course,
                        "class_manager": class_manager,
                        "class_submanager": class_submanager,
                        "class_studentnumber": int(class_studentnumber),
                    },
                )
                return JsonResponse({"sucess": "・更新しました。1"})
            else:
                if ClassGroup.objects.filter(class_name=class_name).count() == 0:
                    ClassGroup.objects.update_or_create(
                        id=pk,
                        defaults={
                            "class_name": class_name,
                            "class_course": class_course,
                            "class_manager": class_manager,
                            "class_submanager": class_submanager,
                            "class_studentnumber": int(class_studentnumber),
                        },
                    )
                    return JsonResponse({"sucess": "・更新しました。1"})
                else:
                    return JsonResponse({"error": "・クラス名は既存しました。"})

        else:
            return JsonResponse({"error": "・クラス名は既存しました。"})

    # except:
    #     return JsonResponse({"error": "somthing wrong right here"})

    # データの取得
    def get(self, request, format=None):
        post_models = PostModels.objects.all()
        post_models = PostModelsSerializer(post_models, many=True)
        return JsonResponse(post_models.data, safe=False)

class DeleteClassSchool(APIView):
    def delete(self, request, pk, format=None):
        user = self.request.user
        if check_user_type_type(user) == "2":
            try:
                class_group = ClassGroup.objects.get(pk=pk)
                class_group.delete()
                return JsonResponse({"success": "School group be deleted"})
            except:
                return JsonResponse({"error": "u can not deleted this group"})


# 掲示板の削除
class DeletePostView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        user = self.request.user
        if check_user_type_type(user) == "2":
            try:
                post_models = PostModels.objects.get(pk=pk)
                post_models.delete()
                return JsonResponse({"success": "Post models be deleted"})
            except:
                return JsonResponse({"error": "u can not deleted this post"})

# 掲示板の閲覧
class ShowPostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, str, format=None):
        user = self.request.user
        create_content = PostModels.objects.filter(created_by_id=str)
        create_content_id = PostModelsSerialier(create_content, many=True)
        return JsonResponse(create_content_id.data, safe=False)
