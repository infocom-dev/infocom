"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include

from rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
# google
from backend.api import views

from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.api.urls')),

    path('auth/', include('rest_auth.urls')),

    path('registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(), ),
    path('registration/', include('rest_auth.registration.urls')),
    path('registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # vk
    path('auth/', include('rest_framework_social_oauth2.urls')),

    # google

    path('google/', views.GoogleLogin.as_view(), name='google_login')
]

urlpatterns += doc_url
