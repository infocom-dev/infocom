from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#     phone = models.CharField(max_length=12)
#     full_name = models.CharField(max_length=255)
#     home_country = models.CharField(max_length=100)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email


# class Customer(CustomUser):
#     business_name = models.CharField(max_length=100)


# class Developer(CustomUser):
#     stack = models.ManyToManyField("AnswersOption")
#     experience = models.TextField()
#     respect = models.IntegerField(default=0)


# class Project(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

#     # ALL PRICES IN $$$
#     predicted_price = models.IntegerField(blank=True, null=True)
#     real_price = models.IntegerField(blank=True, null=True)

#     start_date = models.DateField(blank=True, null=True)
#     predict_end_date = models.DateField(blank=True, null=True)
#     real_end_date = models.DateField(blank=True, null=True)


# class QuestionType(models.TextChoices):
#     SELECTED = 'selected'
#     RANGE = 'range'
#     TEXTAREA = 'textarea'
#     MESSAGE = 'message'
#     DATAPICKER = 'datapicker'
#     SWITCH = 'switch'


# class Question(models.Model):
#     tag = models.CharField("Тег (Суть)", max_length=100, primary_key=True)
#     text = models.TextField("Текст вопроса")
#     type = models.TextField(choices=QuestionType)


# class CustomerAnswer(models.Model):
#     date = models.DateField(blank=True, null=True)
#     text = models.TextField(blank=True, null=True)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="customer_answers")


# class AnswersOption(models.Model):
#     value = models.TextField("Значение варианта ответа в виде текста")
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers_option')
#     customer_answer = models.ManyToManyField(CustomerAnswer, related_name="selected_answers_option")


# x = {
#     "customer_id": 1,
#     "customer_answers": [{
#         "text": "mera one luv <3",
#         "question": {
#             "tag": "project_name"
#         }
#     }]
# }
