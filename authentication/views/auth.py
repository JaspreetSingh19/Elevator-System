from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.serializers.auth import LoginSerializer, LogoutSerializer
from common.messages import SUCCESS_MESSAGES


class LoginViewSet(viewsets.ModelViewSet):
    """
    Allow only authenticated user to signin.
    If the user is valid provide him the access and refresh token
    and save it to the database.
    """
    http_method_names = ['post']
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        """
        Create method to provide access token and refresh
        token to the authenticated user by checking their
        credentials.
        """
        serializer = self.serializer_class(data=request.data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            employee = serializer.create(serializer.validated_data)
            return Response(
                {'data': employee, 'success': SUCCESS_MESSAGES['login']['success']}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class LogoutViewSet(viewsets.ModelViewSet):
    """
    Allow only signin user to sign out
    This Api perform the functionality to blacklist the refresh
    token to avoid access of unauthenticated user
    """
    http_method_names = ['post']
    serializer_class = LogoutSerializer
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        """
        Create method to blacklist the refresh token
        of the signin user.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.create(serializer.validated_data)
            return Response(
                {'data': data, 'success': SUCCESS_MESSAGES['logout']['success']}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
