from django.urls import path,include

from backend.api import views

urlpatterns = ([
    path("getQuestions/", views.QuestionViewSet.as_view({'get': 'list'})),
    path("createQuestion/", views.QuestionViewSet.as_view({'post': 'create'})),
    path('auth/', include('djoser.urls')),
    # path("auth/token/", obtain_auth_token,name='token'),

    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    
])