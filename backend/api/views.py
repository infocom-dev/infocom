from rest_framework import viewsets,permissions

from backend.api.models import Question
from backend.api.serializer import QuestionSerializer




class QuestionViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    
    
    
