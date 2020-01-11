# DRF Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

# Model Imports
from api.models import (User)

# Utils Import
from api.utils.generic import (HashPassword)


class UserLogin(APIView):

    @staticmethod
    def post(request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            if not (email and password):
                return Response(data={"message": "Missing Parameters"}, status=status.HTTP_400_BAD_REQUEST)
            user_obj = User.objects.filter(email=email)
            if not user_obj:
                return Response(data={"message": "Invalid Email."}, status=status.HTTP_400_BAD_REQUEST)
            hashed_password = user_obj.values_list("password", flat=True).first()
            check_password = HashPassword(password=password).verify_hash(_hash=hashed_password)
            if not check_password:
                return Response(data={"message": "Wrong Password."}, status=status.HTTP_401_UNAUTHORIZED)
            user_details = user_obj.values("id", "name", "email").first()
            """Token based system need to be implemented."""
            return Response({"result": {"user_details": user_details, "token": ""}})
        except APIException:
            return Response(data={"error": APIException}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
