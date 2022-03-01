from django.contrib.auth import get_user_model
from django.forms import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import datetime


# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('userID','email','username', 'password', 'name', 'isAdmin')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
        read_only_fields = ('userID', 'isAdmin')

    def create(self, validated_data):
        return get_user_model().objects.createUser(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


# Update user
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name','username' )
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8,'required': False,},
                        'email': {'required': False,},
                        'name': {'required': False,},}

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user





# User information
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('userID','username',  'email', 'name', 'isAdmin')
        read_only_fields = ('userID','email', 'name','username',  'isAdmin')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        
        return data
       
        


# User login
class UserTokenSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        token['userID'] = user.userID
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['access'] = str(refresh.access_token)

        return data





