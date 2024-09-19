
from django.urls import include, path
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'api-v1'
urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(),name='registration'),
    # change password
    # reset password
    # login token
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name='token-logout'),
    # login jwt
    path('jwt/create', TokenObtainPairView.as_view(), name='jwt-create'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify',TokenVerifyView.as_view(), name='jwt_verify')
]