from django.urls import path

from backend.api import views

urlpatterns = ([
    path("hello/", views.QuestionViewSet.as_view({'get': 'list'})),
])