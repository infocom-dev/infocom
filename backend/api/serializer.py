from rest_framework import serializers

from backend.api.models import AnswersOption, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswersOption
        exclude = ("question", "id")


class QuestionSerializer(serializers.ModelSerializer):
    answers_option = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('tag', 'text', 'type', 'answers_option')

    def create(self, validated_data):
        answers_option_data = validated_data.pop('answers_option')
        question = Question.objects.create(**validated_data)
        for answer in answers_option_data:
            AnswersOption.objects.create(question=question, **answer)
        return question
