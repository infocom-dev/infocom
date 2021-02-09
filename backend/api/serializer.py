from rest_framework import serializers

from backend.api.models import QuestionType, Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ("id",)

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionType
        exclude=("id",)

class QuestionSerializer(serializers.ModelSerializer):
    QuestionType = QuestionTypeSerializer()
    Answer=AnswerSerializer(many=True)

    class Meta:
        model = Question
