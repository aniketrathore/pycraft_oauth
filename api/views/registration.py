# DRF Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Model Imports
from api.models import (User)

# Utils Import
from api.utils.generic import (HashPassword)


class UserRegistration(APIView):

    @staticmethod
    def post(request):
        name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")
        if not (name and email and password):
            return Response(data={"message": "Missing Parameters."}, status=status.HTTP_400_BAD_REQUEST)
        email = email.lower()
        if User.objects.filter(email=email):
            return Response(data={"message": "Email already exits."}, status=status.HTTP_400_BAD_REQUEST)
        _hash = HashPassword(password=password).get_hash()
        User.objects.create(name=name, email=email, password=_hash)
        return Response(data={"result": {"message": "Successful created."}}, status=status.HTTP_201_CREATED)
