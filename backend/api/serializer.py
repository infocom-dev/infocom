from rest_framework import serializers

from backend.api.models import QuestionType, Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ("question",)

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= QuestionType
        exclude = ("question",)

class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()
    answer=AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'
