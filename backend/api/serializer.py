from rest_framework import serializers

from backend.api.models import AnswersOption, Question, Customer, Developer, Project


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


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerSerializerEmail(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "email"

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializerEmail(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
