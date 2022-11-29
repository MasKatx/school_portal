from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import UserAccount
from .serializers import UserCreateSerializer

# Create your views here.
class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        users = UserAccount.objects.all()
        users = UserCreateSerializer(users, many=True)
        return Response(users.data)
