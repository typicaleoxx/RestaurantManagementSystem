from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import GroupSerializer
from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get("password")
            hashed_password = make_password(password)
            serializer.save(password=hashed_password)
            return Response({"message": "User created successfully"})
        else:
            return Response(serializer.errors)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "message": " Login Successfull",
                    "token": token.key,
                    "user": UserSerializer(user).data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
class UserDeleteView(generics.DestroyAPIView):
    queryset=User.objects.all
    serializer_class=UserSerializer
    permission_classes = [IsAuthenticated]
