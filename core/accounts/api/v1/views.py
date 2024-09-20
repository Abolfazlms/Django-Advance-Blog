from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from accounts.models import Profile
from django.contrib.auth import get_user_model

from .serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
)

from django.core.mail import send_mail
from mail_templated import EmailMessage, send_mail

from ..utils import EmailThread

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()
class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data={
                'email':serializer.validated_data['email']
            }
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(data,status=status.HTTP_201_CREATED)
        # return self.create(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer
   
class ChangePasswordApiView(generics.GenericAPIView):
    model = User
    permission_class = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            # check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password":["Wrong password."]}, status = status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({'details':['password changed successfully.']},status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        query_set = self.get_queryset()
        obj = get_object_or_404(query_set, user=self.request.user)
        return obj
class TestEmailSend(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "from@example.com",
        #     ["to@example.com"],
        #     fail_silently=False,
        # )        
        # send_mail('email/hello.tpl', {'name': 'ali'}, 'admin@admin.com', ['testmail@gmail.com'])
        self.email = 'admin@admin.com'
        user_obj = get_object_or_404(User, email = self.email)
        token = self.get_tokens_for_user(user_obj)
        email_obj = EmailMessage('email/hello.tpl', {'token': token}, 'admin@admin.com', to=[self.email])
        EmailThread(email_obj).start()

        return Response("email sent.")
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

