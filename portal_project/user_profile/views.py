from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from accounts.models import UserAccount
from .models import UserProfile

# serializer
from .serializers import UserProfileSerializer

# from django.http import HttpResponse


class GetUserProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        try:

            user = request.user
            user_profile = UserProfile.objects.filter(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({"profile": user_profile.data})
        except:
            return Response(
                {"error": "Something went wrong when retrieving profile", "value": user}
            )


class UpdateUserProfileView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user = self.request.user
            username = user.username

            data = self.request.data
            name = data["name"]
            phone = data["phone"]
            avatar = data["avatar"]
            address = data["address"]
            date_of_birth = data["date_of_birth"]
            group_name = data["group_name"]
            user_type = data["user_type"]
            teacher_library = data["teacher_library"]

            UserProfile.objects.update_or_create(
                name=name,
                phone=phone,
                avatar=avatar,
                address=address,
                date_of_birth=date_of_birth,
                group_name=group_name,
                user_type=user_type,
                teacher_library=teacher_library,
            )

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({"profile": user_profile.data, "username": str(username)})
        except:
            return Response({"error": "Something went wrong when updating profile"})
