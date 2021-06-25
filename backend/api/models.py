from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=765, blank=True, default="name")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=16)
    full_name = models.CharField(max_length=255)
    home_country = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Customer(CustomUser):
    business_name = models.CharField(max_length=100)


class Stack(models.Model):
    name = models.CharField("Название технологии", max_length=150, default="Django", primary_key=True)
    avg_price=models.FloatField(blank=True, null=True)
    avg_days=models.IntegerField(blank=True,null=True)


class Project(models.Model):
    name = models.CharField("Название Проекта", max_length=150, default="test project", null=True, blank=True)
    customer = models.ForeignKey(Customer, related_name='projects', on_delete=models.CASCADE,null=True, blank=True)
    stack = models.ForeignKey(Stack, related_name='projects', on_delete=models.CASCADE,null=True, blank=True)
    is_active = models.BooleanField(default=True)
    predicted_price = models.IntegerField(blank=True, null=True)
    real_price = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    predict_end_date = models.DateField(blank=True, null=True)
    real_end_date = models.DateField(blank=True, null=True)


class QuestionType(models.TextChoices):
    SELECTED = 'selected'
    RANGE = 'range'
    TEXTAREA = 'textarea'
    MESSAGE = 'message'
    DATAPICKER = 'datapicker'
    SWITCH = 'switch'
    CHECKBOX = 'checkbox'


class Question(models.Model):
    tag = models.CharField("Тег (Суть)", max_length=100, primary_key=True)
    text = models.TextField("Текст вопроса")
    type = models.TextField(choices=QuestionType.choices)


class CustomerAnswer(models.Model):
    date = models.DateField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    custom_answer = models.ManyToManyField("AnswersOption", related_name="selected_answers_option",blank=True,null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="customer_answers")


class AnswersOption(models.Model):
    value = models.TextField("Значение варианта ответа в виде текста")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers_option')
