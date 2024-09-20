
from django.urls import include, path
from .. import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(),name='registration'),
    path('test-email/', views.TestEmailSend.as_view(),name='test-email'),

    # activation
    path('activation/confirm/<str:token>',views.ActivationAPIView.as_view(),name='activation'),
    

    # resend activation
    path('activation/resend/',views.ActivationResendAPIView.as_view(),name='activation-resend'),

    # change password
    path('password-change',views.ChangePasswordApiView.as_view(),name='change-password'),
    
    # reset password

    # login token
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name='token-logout'),

    # login jwt
    path('jwt/create', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify',TokenVerifyView.as_view(), name='jwt_verify'),
]