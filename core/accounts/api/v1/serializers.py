from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class RegistrationSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(max_length=255,write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password','password1']
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({'detail':'passwords doesn\'t match.'})
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
                raise serializers.ValidationError({'password':list(e.messages)})

        return super().validate(attrs)
    
    def create(self, validate_data):
        validate_data.pop('password1',None)
        return User.objects.create_user(**validate_data)

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
     def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data['email'] = self.user.email
        validated_data['user_id'] = self.user.id
        print(validated_data)
        return validated_data
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)
    new_password1 = serializers.CharField(required = True)

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password1'):
            raise serializers.ValidationError({'detail':'passwords doesn\'t match.'})
        try:
            validate_password(attrs.get('new_password'))
        except exceptions.ValidationError as e:
                raise serializers.ValidationError({'new_password':list(e.messages)})

        return super().validate(attrs)
