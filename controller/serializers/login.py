from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        
        return user

    class Meta:
        model = UserModel
        fields = ('id','username','password','email',)


class UserSerializerProfil(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ('id','password','email')