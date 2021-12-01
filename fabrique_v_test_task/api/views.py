from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from django.utils.timezone import utc

from .models import Question, Quiz
from .serializers import QuestionSerializer, QuizSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def list_of_available(self, request):
        now = datetime.utcnow().replace(tzinfo=utc)
        quiz = Quiz.objects.filter(finished_at__gt=now)
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)

    def questions(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        questions = Question.objects.filter(quiz=quiz)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
