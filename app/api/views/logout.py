# Standard Imports
import requests

# DRF Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Credential Imports
from credential import *


class UserLogOut(APIView):
    @staticmethod
    def post(request):
        try:
            token = request.data.get("token")
            if not token:
                return Response(
                    data={"message": "Token Missing."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            payload = {
                "token": token,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            }
            r = requests.post("http://0.0.0.0:8000/oauth/revoke_token/", data=payload)
            if r.status_code == 200:
                response, status_code = (
                    {"result": {"message": "Successfully Logout."}},
                    status.HTTP_200_OK,
                )
            else:
                response, status_code = r.json(), r.status_code
            return Response(data=response, status=status_code)
        except Exception as e:
            return Response(
                data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
