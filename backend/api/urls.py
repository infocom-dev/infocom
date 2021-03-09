from django.urls import path, include

from backend.api import views

urlpatterns = ([
    # Questions
    path("getQuestions/", views.QuestionViewSet.as_view({'get': 'list'})),
    path("createQuestion/", views.QuestionViewSet.as_view({'post': 'create'})),
    # Customer
    path("createCustomer/", views.CustomerViewSet.as_view({'post': 'create'})),
    path("getCustomers/", views.CustomerViewSet.as_view({'get': 'list'})),

    # Developer
    path("createDeveloper/", views.DeveloperViewSet.as_view({'post': 'create'})),
    path("getDevelopers/", views.DeveloperViewSet.as_view({'get': 'list'})),

    # Project
    path("createProject/", views.ProjectViewSet.as_view({'post': 'create'})),
    path("getProjects/", views.ProjectViewSet.as_view({'get': 'list'})),

    path('auth/', include('djoser.urls')),
    # path("auth/token/", obtain_auth_token,name='token'),

    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

])
