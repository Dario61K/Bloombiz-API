# thirdPartyApps

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from decouple import config as env

# directory

from ..models import User
from .serializers import (
    CreateAccountRequestSerializer,
    EmailSerializer,
    PasswordSerializer
)
from ..notifications.emailNotification import EmailNotification

# base_modules

from typing import Dict, Any
import jwt
import datetime

class CreateAccountRequest(APIView):

    def post(self, request, *args, **kwargs):

        serialized = CreateAccountRequestSerializer(data=request.data)
        if not serialized.is_valid():
            return Response({
                'error' : 'Invalid data',
                'details' : serialized.errors
            }, status=400)
        data: Dict[str:Any] = serialized.validated_data # type: ignore

        if User.objects.filter(email=data.get('email')).exists():
            return Response({
                'error' : 'Email already in use'
            }, status=400)

        exp_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        token = jwt.encode(
            {
                'data' : data,
                'exp' : exp_time
            },
            env('SECRET_KEY'),
            algorithm='HS256'
        )

        try:
            EmailNotification().create_account_notification(data.get('email'), token)
        except Exception as e:
            return Response({
                'error' : f'Failed to send "create account" email: {e}'
            }, status=500)
        
        return Response({
            'message' : f'Confirmation email sent to {data.get("email")}'
        }, status=200)



class CreateAccountConfirm(APIView):

    def post(self, request, token, *args, **kwargs):

        try:
            payload = jwt.decode(token, env('SECRET_KEY'), algorithms=['HS256']) # type: ignore
        except (jwt.InvalidTokenError, jwt.ExpiredSignatureError):
            return Response({
                'error' : 'Invalid token'
            }, status=400)
        
        user_info = payload.get('data')

        try:
            User.objects.create_user(**user_info) #type: ignore
        except Exception as e:
            return Response({
                'error' : f'Failed to create account: {e}'
            }, status=500)

        return Response({
            'message' : "Account created"
        }, status=201)

class ResetPasswordRequest(APIView):

    def post(self, request, *args, **kwargs):
        
        serialized = EmailSerializer(data=request.data)
        if not serialized.is_valid():
            return Response({
                'error' : "Invalid data",
                'details' : serialized.errors 
            },status=400)
        data: Dict[str:Any] = serialized.validated_data # type: ignore
        
        if not User.objects.filter(email=data.get('email')).exists():
            return Response({
                'error' : "No account registred with this email"
            }, status=404)
        
        exp_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        token = jwt.encode({
            'data' : data.get('email'),
            'exp' : exp_time
        }, env('SECRET_KEY'),
        algorithm='HS256')

        try:
            EmailNotification().reset_password_notification(data.get('email'), token)
        except Exception as e:
            return Response({
                'error' : f'Failed to send "reset password" email: {e}'
            }, status=500)
        
        return Response({
            'message' : f'Reset Password email sent to {data.get("email")}',
        }, status=200)



class ResetPasswordVerify(APIView):

    def get(self, request, token, *args, **kwargs):

        try:
            jwt.decode(token, env('SECRET_KEY'), algorithms=['HS256']) # type: ignore
        except (jwt.InvalidTokenError, jwt.ExpiredSignatureError) as e:
            return Response({
                'error' : 'Invalid token',
                'detail' : str(e)
            }, status=400) 
        
        return Response({
            'message' : 'Valid token'
        }, status=200)

class ResetPasswordChange(APIView):

    def put(self, request, token, *args, **kwargs):

        try:
            payload = jwt.decode(token, env('SECRET_KEY'), algorithms=['HS256']) # type: ignore
        except (jwt.InvalidTokenError, jwt.ExpiredSignatureError) as e:
            return Response({
                'error' : 'Invalid token',
                'detail' : str(e)
            }, status=400)

        serialized = PasswordSerializer(data=request.data)
        if not serialized.is_valid():
            return Response({
                'error' : 'Invalid data',
                'details' : serialized.errors
            }, status=400)
        data: Dict[str:Any] = serialized.validated_data # type: ignore

        email = payload.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                'error' : "User not found"
            }, status=404)
        user.set_password(data.get('password'))
        user.save()

        return Response({
            'message' : 'Password reset succefully'
        },status=200)


class ProtectedAPIView(APIView):

    """Base class for views that require JWT authentication."""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class ChangeName(ProtectedAPIView):

    def put(self, request, *args, **kwargs):
        ...

class ChangePassword(ProtectedAPIView):

    def put(self, request, *args, **kwargs):
        ...

class ChangeEmailRequest(ProtectedAPIView):

    def get(self, request, *args, **kwargs):
        ...

class ChangeEmailConfirm(ProtectedAPIView):

    def put(self, request, *args, **kwargs):
        ...

class DeleteAccount(ProtectedAPIView):

    def delete(self, request, *args, **kwargs):
        ... 