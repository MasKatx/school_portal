from django.shortcuts import render
from rest_framework.views import APIView
from .pusher import pusher_client
from django.http import JsonResponse

# Create your views here.
class MessageAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        user = self.request.user
        data = self.request.data
        pusher_client.trigger(
            "chat",
            "message",
            {
                "username": user.username,
                "message": data["message"],
            },
        )

        return JsonResponse({"success": "success to send message"})
