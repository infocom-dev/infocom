from django.urls import path, include
from rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

from backend.api import views

urlpatterns = ([
    # Questions
    path("getQuestions/", views.QuestionViewSet.as_view({'get': 'list'})),
    path("createQuestion/", views.QuestionViewSet.as_view({'post': 'create'})),
    path("getQuestionById/<int:pk>", views.QuestionViewSet.as_view({'get': 'retrieve'})),
    path("deleteQuestion/<int:pk>", views.QuestionViewSet.as_view({'delete': 'destroy'})),

    # Customer
    path("createCustomer/", views.CustomerViewSet.as_view({'post': 'create'})),
    path("getCustomers/", views.CustomerViewSet.as_view({'get': 'list'})),
    path("updateCustomer<int:pk>", views.CustomerViewSet.as_view({'put': 'update'})),
    path("getCustomerById/<int:pk>", views.CustomerViewSet.as_view({'get': 'retrieve'})),
    path("deleteCustomer/<int:pk>", views.CustomerViewSet.as_view({'delete': 'destroy'})),

    # Project
    path("createProject/", views.ProjectViewSet.as_view({'post': 'create'})),
    path("createProjectWithCustomerAnswer/", views.ProjectWithCustomerAnswerViewSet.as_view({'post': 'create'})),
    path("deleteProject/<int:pk>", views.ProjectViewSet.as_view({'delete': 'destroy'})),
    path("updateProject/<int:pk>", views.ProjectViewSet.as_view({'put': 'update'})),
    path("getProjects/", views.ProjectViewSet.as_view({'get': 'list'})),
    path("getProjectById/<int:pk>", views.ProjectViewSet.as_view({'get': 'retrieve'})),

    path("getProjectsActive/", views.ProjectActiveViewSet.as_view({'get': 'list'})),
    path("getProjectsNoActive/", views.ProjectNoActiveViewSet.as_view({'get': 'list'})),

    path("createStack/", views.StackViewSet.as_view({'post': 'create'})),
    path("getStacks/", views.StackViewSet.as_view({'get': 'list'})),
    path("deleteStack/<int:pk>", views.StackViewSet.as_view({'delete': 'destroy'})),

    path("getAvgStack<str:pk>/", views.StackAvgViewSet.as_view({'get': 'retrieve'})),

    #Auth

    path('auth/', include('rest_auth.urls')),

    path('registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(), ),
    path('registration/', include('rest_auth.registration.urls')),
    path('registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # vk
    path('auth/', include('rest_framework_social_oauth2.urls')),



])
