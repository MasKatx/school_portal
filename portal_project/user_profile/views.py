from django.shortcuts import render

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# from rest_framework
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import datetime

# django
from django.http import JsonResponse

# models
from accounts.models import UserAccount
from .models import UserProfile, UserAvatar
from portal.models import SchoolGroup, ClassGroup

# serializer
from .serializers import (
    UserProfileSerializer,
    UserAvatarSerializer,
    StudentProfileSerializer,
)
from accounts.serializers import UserCreateSerializer


# 学生アカウントの削除
def check_user_type(user):
    user_profile = UserProfile.objects.get(user_id=user.id)
    return user_profile.user_type


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


class GetAdminProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = self.request.user
            admin = UserAccount.objects.get(id=int(user.be_remove))
            admin = UserProfile.objects.get(user_id=admin.id)
            admin = UserProfileSerializer(admin)
            return JsonResponse(admin.data)
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
            manager = data["fullname"]
            group_phone = data["phone"]
            group_address = data["address"]
            group_name = data["all_group_name"]
            if request.method == "PUT":
                UserProfile.objects.update_or_create(
                    id=user_id,
                    defaults={
                        "fullname": manager,
                        "phone": group_phone,
                        "address": group_address,
                        "all_group_name": group_name,
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

    def put(self, request, pk, format=None):
        print(pk)
        try:
            avatar = request.data["avatar"]
            print(avatar)
            UserAvatar.objects.update_or_create(
                user_id=pk,
                defaults={"avatar": avatar},
            )
            return JsonResponse({"success": "img was updated"}, status=200)
        except:
            return JsonResponse({"error": "something wrong when updating user avatar"})


class GetAllTeachersAccountProfile(APIView):
    permissiom_classes = [IsAuthenticated]

    def get(self, request, foramt=None):
        user_list = []
        user = self.request.user
        users = UserAccount.objects.filter(be_remove=str(user.id))
        for user in users:
            user_profile = UserProfile.objects.get(user_id=user.id)
            if user_profile.user_type == "2":
                user_list.append(user_profile)
        teacher_account = UserProfileSerializer(user_list, many=True)
        return JsonResponse(teacher_account.data, safe=False, status=200)


class GetAllTeachersAccount(APIView):
    def get(self, request, format=None):
        user = self.request.user
        users = UserAccount.objects.filter(be_remove=str(user.id))
        users = UserCreateSerializer(users, many=True)
        return JsonResponse(users.data, safe=False, status=200)


class CreateTeachersAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

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
        ).sign
        # last user name

        date = datetime.date.today()
        date = str(date).replace("-", "")[2:]

        l_username = UserAccount.objects.latest("id")
        username = f_username + date + str(l_username.id + 1)
        password = teacher_birth.replace("-", "")
        create_user = UserAccount.objects.create_user(email, username, password)
        create_user.be_remove = user.id
        create_user.save()
        user = UserAccount.objects.get(username=username)
        group_name = SchoolGroup.objects.get(group_id=teacher_belong_to_id).group_name
        UserProfile.objects.update_or_create(
            user_id=user.id,
            defaults={
                "fullname": teacher_name,
                "phone": teacher_phone,
                "address": teacher_address,
                "date_of_birth": teacher_birth,
                "teacher_library": teacher_library,
                "teacher_belong_to_name": group_name,
                "teacher_belong_to_id": teacher_belong_to_id,
                "teacher_course": teacher_course,
                "teacher_sex": teacher_sex,
                "user_type": "2",
            },
        )
        return JsonResponse({"success": "created"})


class UpdateTeachersAccountView(APIView):
    def put(self, request, pk, format=None):
        user = self.request.user
        data = self.request.data
        teacher_name = data["fullname"]
        teacher_phone = data["phone"]
        teacher_address = data["address"]
        teacher_library = data["teacher_library"]
        teacher_course = data["teacher_course"]
        teacher_sex = data["teacher_sex"]
        teacher_birth = data["date_of_birth"]
        email = data["email"]
        teacher_belong_to_id = data["teacher_belong_to_id"]
        group_name = SchoolGroup.objects.get(group_id=teacher_belong_to_id).group_name
        user = UserAccount.objects.update_or_create(id=pk, defaults={"email": email})
        user_profile = UserProfile.objects.update_or_create(
            user_id=pk,
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
        return JsonResponse({"success": "updated"})


class DeleteTeachersAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        try:
            user = self.request.user
            print(pk)
            user_will_be_deleted = UserAccount.objects.get(
                pk=pk, be_remove=f"{user.id}"
            )
            user_will_be_deleted.delete()
            return JsonResponse({"success": f"deleted by {user}"})
        except:
            return JsonResponse({"error": f"u cant delete {user}"})


# user get all profile avatar by admin(manager)
class GetAllTeacherAvatarByAdmin(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            users = UserAccount.objects.filter(be_remove=user.id).order_by("id")
            student_avt_list = []
            for user in users:
                if check_user_type(user) == "2":
                    user_avt = UserAvatar.objects.get(user_id=user.id)
                    student_avt_list.append(user_avt)
            users_avatar = UserAvatarSerializer(student_avt_list, many=True)
            return JsonResponse(users_avatar.data, safe=False)

        except:
            return JsonResponse({"error": "somthing wrong right here"})


# 学生アカウントの作成
class CreateStudentsAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:

            user = self.request.user
            data = self.request.data
            student_name = data["fullname"]
            student_phone = data["phone"]
            student_address = data["address"]
            student_gender = data["teacher_sex"]
            student_birth = data["date_of_birth"]
            student_name_furigana = data["student_fullname_furigana"]
            student_post_num = data["student_post_num"]
            student_class_id = data["student_class_name"]
            student_department_name = data["student_department_name"]
            student_field_name = data["student_field_name"]
            try:
                email = data["email"]
            except:
                return JsonResponse({"error": "・このメールアドレスは既存しました。"})

            user_profile = UserProfile.objects.get(user_id=user.id)
            group_school = SchoolGroup.objects.get(
                group_id=user_profile.teacher_belong_to_id
            )
            f_username = group_school.sign
            date = datetime.date.today()
            date = str(date).replace("-", "")[2:]

            l_username = UserAccount.objects.latest("id")
            username = f_username + date + str(l_username.id + 1)
            password = student_birth.replace("-", "")

            create_user = UserAccount.objects.create_user(email, username, password)
            create_user.be_remove = user.be_remove
            create_user.save()
            user = UserAccount.objects.get(username=username)
            UserProfile.objects.update_or_create(
                user_id=user.id,
                defaults={
                    "fullname": student_name,
                    "phone": student_phone,
                    "address": student_address,
                    "date_of_birth": student_birth,
                    "teacher_sex": student_gender,
                    "teacher_belong_to_id": group_school.group_id,
                    "teacher_belong_to_name": group_school.group_name,
                    "student_department_name": student_department_name,
                    "student_class_name": student_class_id,
                    "student_fullname_furigana": student_name_furigana,
                    "student_field_name": student_field_name,
                    "student_post_num": student_post_num,
                    "user_type": "3",
                },
            )
            return JsonResponse({"success": "created Student Account"})
        except:
            return JsonResponse({"error": "something wrong right here"})


class DeleteStudentAccountView(APIView):
    permission_classes = [IsAuthenticated]

    # get, put, post, delete
    def delete(self, request, pk, format=None):
        user = self.request.user
        # 先生 => be_remove, username, email....
        if check_user_type(user) == "2":
            user_will_be_deleted = UserAccount.objects.get(
                pk=pk, be_remove=user.be_remove
            )
            user_will_be_deleted.delete()
            return JsonResponse({"success": f"{user}を消しました。"})
        else:
            return JsonResponse({"error": f"{user}を消すことはできません。"})


# 学生アカウント一覧
class GetStudentAccountsProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = self.request.user
            if check_user_type(user) == "2":
                user_belong_school_id = UserProfile.objects.get(
                    user_id=user.id
                ).teacher_belong_to_id

                studentaccounts = UserProfile.objects.filter(
                    teacher_belong_to_id=user_belong_school_id,
                    user_type="3",
                ).order_by("user_id")
                studentaccounts_id = StudentProfileSerializer(
                    studentaccounts, many=True
                )
                return JsonResponse(studentaccounts_id.data, safe=False)
            return JsonResponse({"error": "アクセス権利を持っていません。"})
        except:
            return JsonResponse({"error": "somthing wrong when u access on this api"})


class UpdateStudentsAccountView(APIView):
    def put(self, request, pk, format=None):
        try:
            user = self.request.user
            data = self.request.data
            student_name = data["fullname"]
            student_phone = data["phone"]
            student_address = data["address"]
            student_gender = data["teacher_sex"]
            student_birth = data["date_of_birth"]
            student_name_furigana = data["student_fullname_furigana"]
            student_post_num = data["student_post_num"]
            student_class_id = data["student_class_name"]
            student_department_name = data["student_department_name"]
            student_field_name = data["student_field_name"]
            try:
                email = data["email"]
            except:
                return JsonResponse({"error": "・このメールアドレスは既存しました。"})
            user = UserAccount.objects.update_or_create(
                id=pk, defaults={"email": email}
            )
            user_profile = UserProfile.objects.update_or_create(
                user_id=pk,
                defaults={
                    "fullname": student_name,
                    "phone": student_phone,
                    "address": student_address,
                    "date_of_birth": student_birth,
                    "teacher_sex": student_gender,
                    "student_department_name": student_department_name,
                    "student_class_name": student_class_id,
                    "student_fullname_furigana": student_name_furigana,
                    "student_field_name": student_field_name,
                    "student_post_num": student_post_num,
                    "user_type": "3",
                },
            )
            return JsonResponse({"success": "updated"})

        except:
            return JsonResponse({"error": "somthing wrong right here"})


class GetStudentAvatarProfile(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            user = UserAccount.objects.get(id=user.id)
            user_profile = UserProfile.objects.get(user_id=user.id)
            users_profile = UserProfile.objects.filter(
                teacher_belong_to_id=user_profile.teacher_belong_to_id, user_type="3"
            ).order_by("user_id")
            student_avt_list = []
            for user_profile in users_profile:
                user_avt = UserAvatar.objects.get(user_id=user_profile.user_id)
                student_avt_list.append(user_avt)
            users_avatar = UserAvatarSerializer(student_avt_list, many=True)
            return JsonResponse(users_avatar.data, safe=False)

        except:
            return JsonResponse({"error": "somthing wrong right here"})
