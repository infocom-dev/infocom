from django.shortcuts import render

# Create your views here.
#URL /getAllChatByUser/
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


@api_view(['GET'])
def api_gretting(request):
    return Response({'chats': "Hello"})