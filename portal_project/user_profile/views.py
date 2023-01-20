from django.shortcuts import render

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# from rest_framework
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

# django
from django.http import JsonResponse

# models
from accounts.models import UserAccount
from .models import UserProfile, UserAvatar
from portal.models import SchoolGroup

# serializer
from .serializers import UserProfileSerializer, UserAvatarSerializer
from accounts.models import UserAccount
from portal.models import SchoolGroup


class GetUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = self.request.user
            user = UserAccount.objects.get(id=user.id)
            user_profile = UserProfile.objects.get(user_id=user.id)
            user_profile = UserProfileSerializer(user_profile)
            return JsonResponse(user_profile.data)
        except:
            return JsonResponse({"value": "error"})


class UpdateUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        try:
            user = self.request.user
            user = UserAccount.objects.get(id=user.id)
            user_id = user.id
            data = self.request.data
            manager = data["manager"]
            group_phone = data["group_phone"]
            group_address = data["group_address"]
            group_name = data["group_name"]
            if request.method == "PUT":
                UserProfile.objects.update_or_create(
                    user_id=user_id,
                    defaults={
                        "fullname": manager,
                        "phone": group_phone,
                        "address": group_address,
                        "group_name": group_name,
                    },
                )
                user_profile = UserProfile.objects.get(user_id=user_id)
                user_profile = UserProfileSerializer(user_profile)
                return JsonResponse(user_profile.data)
        except:
            return JsonResponse(
                {"error": "Something went wrong when updating user profile"}
            )


class GetUserAvatarView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = self.request.user
            user = UserAccount.objects.get(id=user.id)
            user_avatar = UserAvatar.objects.get(user_id=user.id)
            user_avatar = UserAvatarSerializer(user_avatar)
            return JsonResponse(user_avatar.data)
        except:
            return JsonResponse({"error": "NoAvatar"})


class UpdateUserAvatarView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, format=None):
        try:
            user = self.request.user
            user = UserAccount.objects.get(id=user.id)
            avatar = request.data["avatar"]
            UserAvatar.objects.update_or_create(
                user_id=user.id,
                defaults={"avatar": avatar},
            )
            # user_avatar = UserAvatarSerializer(avatar=avatar)
            # user_avatar = UserAvatar.objects.get(user_id=user.id)
            return JsonResponse({"success": "img was updated"}, status=200)
        except:
            return JsonResponse({"error": "something wrong when updating user avatar"})


class GetAllTeachersAccount(APIView):
    permissiom_classes = [IsAuthenticated]

    def get(self, request, foramt=None):
        user_list = []
        user = self.request.user
        users = UserAccount.objects.filter(be_remove=str(user.id))
        for user in users:
            user_profile = UserProfile.objects.get(id=user.id)
            user_list.append(user_profile)
        print(user_list)
        teacher_account = UserProfileSerializer(user_list, many=True)
        return JsonResponse(teacher_account.data, safe=False, status=200)


class CreateTeachersAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return UserAccount.objects.filter()

    def post(self, request, format=None):
        try:

            user = self.request.user
            data = self.request.data
            teacher_name = data["teacher_name"]
            teacher_phone = data["teacher_phone"]
            teacher_address = data["teacher_address"]
            teacher_library = data["teacher_library"]
            teacher_course = data["teacher_course"]
            teacher_sex = data["teacher_sex"]
            teacher_birth = data["teacher_birth"]
            email = data["teacher_email"]
            teacher_belong_to_id = data["teacher_belong_to_id"]
            # first user name
            f_username = SchoolGroup.objects.get(
                user_id=user.id, group_id=teacher_belong_to_id
            ).group_id
            # last user name
            l_username = UserAccount.objects.filter(be_remove=str(user.id)).count()
            username = f_username + str(l_username)

            password = teacher_birth.replace("-", "")
            create_user = UserAccount.objects.create_user(email, username, password)
            create_user.be_remove = user.id
            create_user.save()
            user = UserAccount.objects.get(username=username)
            group_name = SchoolGroup.objects.get(
                group_id=teacher_belong_to_id
            ).group_name
            user_profile = UserProfile.objects.update_or_create(
                pk=user.id,
                defaults={
                    "fullname": teacher_name,
                    "phone": teacher_phone,
                    "address": teacher_address,
                    "date_of_birth": teacher_birth,
                    "teacher_belong_to_name": group_name,
                    "teacher_belong_to_id": teacher_belong_to_id,
                    "teacher_library": teacher_library,
                    "teacher_course": teacher_course,
                    "teacher_sex": teacher_sex,
                    "user_type": "2",
                },
            )
            user_profile = UserProfile.objects.get(user_id=user.id)
            user_profile = UserProfileSerializer(user_profile)
            print(user_profile)

            return JsonResponse({"success": "created"})
        except:
            return JsonResponse({"error": "somthing wrong"})


class DeleteTeachersAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        try:
            user = self.request.user
            user_will_be_deleted = UserAccount.objects.get(
                pk=pk, be_remove=f"{user.id}"
            )
            user_will_be_deleted.delete()
            return JsonResponse({"success": f"deleted by {user}"})
        except:
            return JsonResponse({"error": f"u cant delete {user}"})


class UpdateTeachersAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        pass


class UpdateUserAccountPassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        user = self.request.user
        data = self.request.data
        UserAccount.objects.update(pk=pk, defaults={})


class CreateStudentsAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return UserAccount.objects.filter()

    def post(self, request, format=None):
        # try:

        user = self.request.user
        data = self.request.data
        student_name = data["student_name"]
        student_number = data["student_number"]
        student_phone = data["student_phone"]
        student_address = data["student_address"]
        student_gender = data["student_gender"]
        student_birth = data["student_birth"]
        student_course = data["student_course"]
        email = data["student_email"]
