from rest_framework import viewsets
from rest_framework.response import Response
from backend.api.serializer import *


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectActiveViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer


class ProjectNoActiveViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_active=False)
    serializer_class = ProjectSerializer


class StackViewSet(viewsets.ModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class StackAvgViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackPricesSerializer

    def retrieve(self, request, *args, **kwargs):
        avg_price = 0
        avg_time = 0
        instance = self.get_object()
        projects = instance.projects.all()
        for project in projects:
            if project.real_price!=None:
                avg_price += project.real_price
            if project.real_end_date!=None:
                avg_time += ((project.real_end_date - project.start_date).days)
        avg_time = int(avg_time / projects.count())
        avg_price = avg_price / projects.count()
        instance.avg_price = avg_price
        instance.avg_days = avg_time
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
