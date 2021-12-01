from datetime import datetime
import uuid

from django.utils.timezone import utc

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import Answer, Question, Quiz
from .serializers import AnswerSerializer, QuestionSerializer, QuizSerializer


def get_or_create_user(user_id: int) -> User:
    try:
        user = User.objects.get(username=user_id)
    except User.DoesNotExist:
        user = User(username=user_id)
        user.save()
    return user


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


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def create(self, request, *args, **kwargs):
        user = get_or_create_user(request.data.get("user"))
        return super().create(request, user=user, *args, **kwargs)


class UserStatViewSet(ViewSet):
    def answers(self, request, user_id):
        answers = Answer.objects.filter(user=get_or_create_user(user_id))
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def passed_quizzes(self, request, user_id):
        user = get_or_create_user(user_id)
        users_answers_ids = Answer.objects.filter(user=user).values("id")
        questions_ids = Question.objects.filter(id__in=users_answers_ids).values("id")
        quizzes_particioated = Quiz.objects.filter(id__in=questions_ids)
        serializer = QuizSerializer(quizzes_particioated, many=True)
        return Response(serializer.data)
