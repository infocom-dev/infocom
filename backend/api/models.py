from django.db import models


# Create your models here.
class Question(models.Model):
    text = models.TextField("Текст вопроса")

class QuestionType(models.Model):
    name = models.CharField("Тип вопроса", max_length=150)
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='type'
    )
    def __str__(self):
        return f"{self.name}"

class Answer(models.Model):
    value=models.TextField("Значение вопроса")
    question=models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answers')