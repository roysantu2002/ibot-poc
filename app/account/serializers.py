"""
Selializers for the user account View.
"""
import logging
import os
import sys
from enum import unique

from account.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer,
                                                  TokenRefreshSerializer)
from rest_framework_simplejwt.tokens import RefreshToken

# logger = logging.getLogger(__name__)
# logger_django = logging.getLogger('django')
# warn_log = logging.getLogger('warn_log')
# logger_ibots = logging.getLogger('ibots_log')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'about', 'is_staff', 'is_active', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    email = serializers.EmailField(required=True)
    # user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            # logger_ibots.error('validate_email')
            exc_type, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # logger_ibots.error(exc_type, fname, exc_tb.tb_lineno)
            # logger_ibots.error(f'Email Already Exists {self.request.session["id"]}')
            raise serializers.ValidationError("Email Already Exists")

        return lower_email

    # def validate_user_name(self, value):
    #     user_name = value.lower()
    #     if User.objects.filter(user_name__iexact=user_name).exists():
    #         raise serializers.ValidationError("User Name Already Exists")
    #     return user_name

    def get_cleaned_data(self):
        super(CustomUserSerializer, self).get_cleaned_data()
        return {
            'email' : self.validated_data.get('email', ''),
            # 'user_name' : self.validated_data.get('user_name', ''),
            'password' : self.validated_data.get('password', '')

        }


    def create(self, validated_data):
        try:
            password = validated_data.pop('password', None)
            # as long as the fields are the same, we can just use this
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
        except :
            raise serializers.ValidationError('User already exists.')

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return

class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        access_token = refresh.access_token
        print(access_token)
        data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
        return data


class TokenRefreshLifetimeSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])
        data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
        return data