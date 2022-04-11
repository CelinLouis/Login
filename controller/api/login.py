from numpy import delete
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from controller.serializers.login import UserSerializer, UserSerializerUpdate,UserSerializerProfil
from rest_framework.authtoken.views import Token
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)


#sign up
class CreateUserAPI(CreateAPIView):
    #permission_classes = [IsAuthenticated]
    model = get_user_model()
    serializer_class = UserSerializer

#login
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data,
                                           context = {'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        })


#logout
class LogOutAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
        except Token.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfil(APIView):
    permission_class = [IsAuthenticated]
    def get(self, request):
        user = User.objects.get(username=request.user)
        user_data = UserSerializerProfil(user).data
        return Response(user_data)
    

    def put(self, request):
        data = request.data
        user = User.objects.get(username=request.user)
        print("User",user)
        serializer = UserSerializerUpdate(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def delete(self, request):
        user = User.objects.get(username=request.user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)