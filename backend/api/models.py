from django.db import models


# Create your models here.
class QuestionType(models.Model):
    name = models.CharField("Тип вопроса", max_length=150)

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    text = models.TextField("Текст вопроса")
    type = models.ForeignKey(QuestionType, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return f"{self.text}"


class Answer(models.Model):
    value = models.TextField("Значение вопроса")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f"{self.value}"
