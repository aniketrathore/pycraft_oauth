# DRF Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Model Imports
from api.models import User

# Utils Import
from api.utils.generic import HashPassword


class UserRegistration(APIView):
    @staticmethod
    def post(request):
        try:
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            username = request.data.get("username")
            email = request.data.get("email")
            password = request.data.get("password")
            if not (email and username and password):
                return Response(
                    data={"message": "Missing Parameters."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            email = email.lower()
            if User.objects.filter(email=email):
                return Response(
                    data={"message": "Email already exits."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if User.objects.filter(username=username):
                return Response(
                    data={"message": "Username already exits."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            _hash = HashPassword(password=password).get_hash()
            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=_hash,
            )
            return Response(
                data={"result": {"message": "Successful created."}},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
