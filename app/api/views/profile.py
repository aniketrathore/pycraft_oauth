# DRF Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication

# OAuth Imports
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserProfileDetails(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["read"]

    @staticmethod
    def get(request):
        try:
            user_id = request.query_params.get("user_id")
            if not user_id:
                return Response(
                    data={"message": "Missing Parameters."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(data={}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
