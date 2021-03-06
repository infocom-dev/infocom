from rest_framework import viewsets,permissions

from backend.api.models import Question
from backend.api.serializer import QuestionSerializer
# 
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class LogoutView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)