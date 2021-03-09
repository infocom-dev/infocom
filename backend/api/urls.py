from django.urls import path,include


from backend.api import views



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenCookieDeleteView,
)



urlpatterns = ([
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/delete/', TokenCookieDeleteView.as_view(), name='token_delete'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

])