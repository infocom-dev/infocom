from rest_framework import viewsets

from backend.api.models import Question
from backend.api.serializer import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    serializers_fieldsets={str:('id')}