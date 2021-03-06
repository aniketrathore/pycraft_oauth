# Standard Imports
import requests

# DRF Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Model Imports
from api.models import User

# Credential Imports
from credential import *


class UserLogin(APIView):
    @staticmethod
    def post(request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            if not (username and password):
                return Response(
                    data={"message": "Missing Parameters"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user_obj = User.objects.filter(username=username)
            if not user_obj:
                return Response(
                    data={"message": "Invalid username."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user_details = user_obj.values("id", "email").first()
            data = {
                "grant_type": "password",
                "username": username,
                "password": password,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            }
            r = requests.post("http://0.0.0.0:8000/oauth/token/", data=data)
            return Response(
                {"result": {"user_details": user_details, "token": r.json()}}
            )
        except Exception as e:
            return Response(
                data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
