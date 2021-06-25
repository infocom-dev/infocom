import pandas
from rest_framework import viewsets, status
from rest_framework.response import Response
from backend.api.serializer import *
from backend.model import *


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectWithCustomerAnswerViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectWithCustomerAnswerSerializer

    def create(self, request, *args, **kwargs):
        try:
            data=convert(request.data.get('customer_answers'))
            data = magic_cost_time_estimator.cook_data(data)
            cost, date = magic_cost_time_estimator.predict(data)
            date = convert_hours_to_date(date)
        except Exception as e:
            print(e, flush=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        request.data['predicted_price'] = int(cost)
        request.data['predict_end_date'] = date
        try:
            for element in range(len(request.data.get('customer_answers'))):
                request.data.get('customer_answers')[element].pop("custom_answer")
        except:
            pass
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except Exception as e:
            print(e, flush=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProjectActiveViewSet(viewsets.ReadOnlyModelViewSet):
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
            if project.real_price != None:
                avg_price += project.real_price
            if project.real_end_date != None:
                avg_time += ((project.real_end_date - project.start_date).days)
        avg_time = int(avg_time / projects.count())
        avg_price = avg_price / projects.count()
        instance.avg_price = avg_price
        instance.avg_days = avg_time
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
