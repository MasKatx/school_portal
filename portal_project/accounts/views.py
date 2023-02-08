from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse
from .models import UserAccount, BaseUserManager
from .serializers import UserCreateSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import (
    BaseUserManager,
)

# Create your views here.

class GetUsersView(APIView):
    """
    サンプルコード：テスト用
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        users = UserAccount.objects.all()
        users = UserCreateSerializer(users, many=True)
        return Response(users.data)


class GetUser(APIView):
    """
    自身のアカウントのプロフィールを全て取得する
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = self.request.user
        user = UserAccount.objects.get(id=user.id)
        user_profile = UserCreateSerializer(user_profile, many=True)
        return JsonResponse({user_profile.data})


# パスワードの変更
class UpdateUserAccountPassword(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        obj = self.request.user
        return obj

    def put(self, request, format=None):
        data = self.request.data
        self.object = self.get_queryset()
        if not self.object.check_password(data["old_password"]):
            print(self.object.check_password(data["old_password"]))
            return JsonResponse({"error": "・パスワードが異なります。"})
        self.object.set_password(data["new_password"])
        self.object.save()
        return JsonResponse({"success": "password be updated"})
        # check_login = UserAccount.objects.get(
        #     id=user.id, password=BaseUserManager.set_password(old_password)
        # )
        # print(check_login)
