from django.urls import path,include


from backend.api import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = ([
    path("hello/", views.QuestionViewSet.as_view({'get': 'list'})),
    path('auth/token/login/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    # path('auth/token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # # Submit your refresh token to this path to obtain a new access token
    # path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/token/logout/', views.LogoutView.as_view(), name='auth_logout'),
    # # path('auth/', include('djoser.urls')),
    # # path("auth/token/", obtain_auth_token,name='token'),


    path('auth/', include('djoser.urls.authtoken')),

    
    
])