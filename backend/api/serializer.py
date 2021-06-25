from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from backend.api.models import AnswersOption, Question, Customer, Project, Stack, CustomerAnswer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class CustomerAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAnswer
        fields = ('date','text','question','custom_answer')

class ProjectWithCustomerAnswerSerializer(serializers.ModelSerializer):
    customer_answers=CustomerAnswerSerializer(
        many=True
    )

    class Meta:
        model = Project
        fields = "__all__"

    def create(self, validated_data):
        customer_answers_data = validated_data.pop('customer_answers')
        project = Project.objects.create(**validated_data)
        for customer_answers_d in customer_answers_data:
            CustomerAnswer.objects.create(project=project, **customer_answers_d)
        return project



class StackSerializer(serializers.ModelSerializer):
    projects = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = Stack
        fields = "__all__"


class StackPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = "__all__"


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
    projects = ProjectSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Customer
        fields = "__all__"


class CustomerSerializerEmail(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "email"


class CustomRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField(max_length=16)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone = self.data.get('phone')
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'email',
            'id',
            'username'
        )
