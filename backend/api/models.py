from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=765, blank=True,default="name")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=12)
    full_name = models.CharField(max_length=255)
    home_country = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Question(models.Model):
    tag = models.CharField("Тег (Суть)", max_length=100, primary_key=True,default="имя")
    text = models.TextField("Текст вопроса")
    type = models.TextField(choices=QuestionType.choices)


class CustomerAnswer(models.Model):
    date = models.DateField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    custom_answer = models.ManyToManyField("AnswersOption", related_name="selected_answers_option")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="customer_answers")


class AnswersOption(models.Model):
    value = models.TextField("Значение варианта ответа в виде текста")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers_option')
