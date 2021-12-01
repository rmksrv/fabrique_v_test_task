from rest_framework import serializers
from ..models import Question


class QuestionListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = [
            "id",
            "answer_type",
            "text",
        ]


class CreateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"
