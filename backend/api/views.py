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
    "text": "Какие задачи должен решать чат-бот?",
    "type": "checkbox",
    "answers": [
      {
        "id": 1,
        "value": "обработка типовых сообщений "
      },
      {
        "id": 2,
        "value": "рассылка подписчикам"
      },
      {
        "id": 3,
        "value": "фильтрация поступающих заявок"
      },
      {
        "id": 4,
        "value": "мгновенная реакция на сообщения "
      }
    ]
  },
  {
    "id": "2",
    "text": "Где  должен размещаться чат-бот?",
    "type": "selected",
    "answers": [
      {
        "id": 1,
        "value": "сайт"
      },
      {
        "id": 2,
        "value": "мессенджеры"
      },
      {
        "id": 3,
        "value": "личный кабинет"
      },
      {
        "id": 4,
        "value": "мессенджеры"
      },
      {
        "id": 5,
        "value": "мобильное  приложение"
      },
      {
        "id": 6,
        "value": "гаджет"
      }

    ]
  },
  {
    "id": "3",
    "text": "Укажите минимальное и максимальное кол-во посетителей приложения, в котором планируется использование чат-бота (для каждого канала)?",
    "type": "range",
    "answers": [0,200]
  },
  {
    "id": "4",
    "text": "any questions",
    "type": "message",
    "answers": []
  }
])