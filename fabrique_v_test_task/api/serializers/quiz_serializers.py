from rest_framework import serializers
from ..models import Quiz
from .question_serializers import QuestionListSerializers


class QuizListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = [
            "id",
            "name",
        ]


class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuestionListSerializers(many=True)

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


class CreateQuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = "__all__"

