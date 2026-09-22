from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    ForgotPasswordView,
    ResetPasswordView,
    ProfileView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgot-password/',ForgotPasswordView.as_view(),name='forgot_password'),
    path('reset-password/',ResetPasswordView.as_view(),name='reset_password'),

    path('profile/', ProfileView.as_view(), name='profile'),
]