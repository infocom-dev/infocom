from django.urls import path,include


from backend.api import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = ([

    path('auth/', include('djoser.urls.authtoken')),

    
    
])