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
    return Response([
  {
    "id": "1",
    "text": "what is your name",
    "type": "selected",
    "answers": [
      {
        "id": 1,
        "value": "Egor"
      },
      {
        "id": 2,
        "value": "Tanya"
      },
      {
        "id": 3,
        "value": "Vitya"
      },
      {
        "id": 4,
        "value": "Zhenya"
      }
    ]
  },
  {
    "id": "2",
    "text": "how are you",
    "type": "radio",
    "answers": [
      {
        "id": 1,
        "value": "ok"
      },
      {
        "id": 2,
        "value": "not ok"
      }
    ]
  },
  {
    "id": "3",
    "text": "any questions",
    "type": "message",
    "answers": []
  }
])