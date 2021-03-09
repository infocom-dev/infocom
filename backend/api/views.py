from rest_framework import viewsets, permissions

from backend.api.models import Question, Customer, Developer, Project
from backend.api.serializer import QuestionSerializer, CustomerSerializer, DeveloperSerializer, ProjectSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer