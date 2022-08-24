from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from custom_auth.serializers import RegisterSerializer


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': str(token.key)})


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        login = request.data.get('login')
        if not User.objects.filter(username=login).exists():
            return Response(f'{login} - does not exists')
        user = User.objects.get(username=login)
        password = request.data.get('password')
        pass_check = check_password(password, user.password)
        if not pass_check:
            return Response('password incorrect')
        token = Token.objects.get(user=user)
        return Response({'token': str(token.key)})

