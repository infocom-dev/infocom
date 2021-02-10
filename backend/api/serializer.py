from rest_framework import serializers

from backend.api.models import QuestionType, Answer, Question
from rest_framework.fields import IntegerField


# class StringArrayField(IntegerField):
#     """
#     String representation of an array field.
#     """
#
#     def to_representation(self, value):
#         return str(value)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ("question",)


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        exclude = ("question",)


class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields=('id','text','type','answers')
