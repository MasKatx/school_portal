from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse
from .models import UserAccount
from .serializers import UserCreateSerializer

# Create your views here.
class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        users = UserAccount.objects.all()
        users = UserCreateSerializer(users, many=True)
        return Response(users.data)


class GetUser(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = self.request.user
        user = UserAccount.objects.get(id=user.id)
        user_profile = UserCreateSerializer(user_profile, many=True)
        return JsonResponse({user_profile.data})
