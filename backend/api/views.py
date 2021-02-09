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
    "type": "selected",
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
    "type": "checkbox",
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
        "value": "мобильное  приложение"
      },
      {
        "id": 5,
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
    "text": "Введидте ожидаемая нагрузку (кол-во обращений) на чат-бота",
    "type": "message",
    "answers": []
  },
  {
    "id": "5",
    "text": "Какой формат диалога предпочтительнее?",
    "type": "checkbox",
    "answers": [
      {
        "id": 1,
        "value": "Свободное общение"
      },
      {
        "id": 2,
        "value": "работа по фиксированному сценарию диалога "
      }
    ]
  },
  {
    "id": "6",
    "text": "На каких языках должен вести диалог чат-бот?",
    "type": "selected",
    "answers": [
      {
        "id": 1,
        "value": "English"
      },
      {
        "id": 2,
        "value": "Russian"
      }
    ]
  },
  { 
    "id": "7",
    "text": "Добавить встроенную платёжную систёма",
    "type": "switch",
    "answers": [{
        "id": 1,
        "value": "Да"
      },
      {
        "id": 2,
        "value": "Нет"
      }]
  },
  { 
    "id": "8",
    "text": "Добавить безопасную сделку",
    "type": "switch",
    "answers": [{
        "id": 1,
        "value": "Да"
      },
      {
        "id": 2,
        "value": "Нет"
      }]
  },
  { 
    "id": "9",
    "text": "Добавить работу с геолокацией",
    "type": "switch",
    "answers": [{
        "id": 1,
        "value": "Да"
      },
      {
        "id": 2,
        "value": "Нет"
      }]
  },
  { 
    "id": "10",
    "text": "Добавить переключение диалога на оператора онлайн-чата по запросу  пользователя",
    "type": "switch",
    "answers": [{
        "id": 1,
        "value": "Да"
      },
      {
        "id": 2,
        "value": "Нет"
      }]
  },
  { 
    "id": "11",
    "text": "Должен ли чат-бот взаимодействовать с другими ботами, сайтами?",
    "type": "switch",
    "answers": [
      {
        "id": 1,
        "value": "Да"
      },
      {
        "id": 2,
        "value": "Нет"
      }
    ]
  },
  { 
    "id": "12",
    "text": "Есть ли у этих систем API? ",
    "type": "switch",
    "answers": [
      {
        "id": 1,
        "value": "Да"
      },
      {
        "id": 2,
        "value": "Нет"
      }
    ]
  },
  {
    "id": "13",
    "text": "Способ  поставки продукта:",
    "type": "selected",
    "answers": [
      {
        "id": 1,
        "value": "SaaS (облачный сервис Инфоком-НН)"
      },
      {
        "id": 2,
        "value": "интеграционный модуль на серверах заказчика"
      },
      {
        "id": 3,
        "value": "полное размещение на серверах заказчика"
      }
    ]
  },
  { 
    "id": "14",
    "text": "Сроки выполнения проекта",
    "type": "datapicker",
    "answers": []
  },
   {
    "id": "15",
    "text": "Укажите бюджет проекта (диапазон):",
    "type": "range",
    "answers": [0,1000]
  },
  {
    "id": "16",
    "text": "Ваши примечания, пожелания, которые не вошли в : нашу анкету",
    "type": "textarea",
    "answers": []
  },
])