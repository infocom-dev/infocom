from django.urls import path,include


from backend.api import views


from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)



urlpatterns = ([
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Submit your refresh token to this path to obtain a new access token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Register a new user
    path('register/', views.register, name='register_view'),

])