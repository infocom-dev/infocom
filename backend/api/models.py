from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=12)
    full_name = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Customer(CustomUser):
    pass


class Technology(models.Model):
    name = models.CharField(max_length=200)


class Developer(CustomUser):
    stack = models.ManyToManyField(Technology, on_delete=models.CASCADE)
    experience = models.TextField()


class Project(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    stack = models.ManyToManyField(Technology, on_delete=models.CASCADE)

    # ALL PRICES IN $$$
    predicted_price = models.IntegerField()
    real_price = models.IntegerField()

    start_date = models.DateField()
    predict_end_date = models.DateField()
    real_end_date = models.DateField()


class QuestionType(models.TextChoices):
    SELECTED = 'selected'
    RANGE = 'range'
    TEXTAREA = 'textarea'
    MESSAGE = 'message'
    DATAPICKER = 'datapicker'
    SWITCH = 'switch'


class Question(models.Model):
    text = models.TextField("Текст вопроса")
    type = models.TextField(choices=QuestionType)


class AnswersOption(models.Model):
    value = models.TextField("Значение вопроса")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')


class UserAnswer(models.Model):
    name = models.CharField("Название (Суть)", max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
