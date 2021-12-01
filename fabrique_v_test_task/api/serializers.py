from rest_framework import serializers
from .models import Quiz, Question, Answer


class GetQuestionListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = [
            "id",
            "answer_type",
            "text",
        ]


class GetQuizListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = [
            "id",
            "name",
        ]


class GetQuizDetailSerializer(serializers.ModelSerializer):
    questions = GetQuestionListSerializers(many=True)

    class Meta:
        model = Quiz
        fields = [
            "id",
            "name",
            "description",
            "started_at",
            "finished_at",
            "questions",
        ]


class CreateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            "text",
            "answer_type",
        )


class CreateQuizSerializer(serializers.ModelSerializer):
    questions = CreateQuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = "__all__"

