from django.urls import include, path
from accounts.views import send_email
app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    # path('api/v1/',include('accounts.api.v1.urls')),
    path("send-email", send_email, name='send-email'),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
]
