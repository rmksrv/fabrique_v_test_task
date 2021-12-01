from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Quiz
from .serializers.question_serializers import CreateQuestionSerializer
from .serializers.quiz_serializers import QuizListSerializer, QuizDetailSerializer, CreateQuizSerializer


class GetAvailableQuizzesView(GenericAPIView):
    serializer_class = QuizListSerializer

    def get(self, request):
        available_quizzes = filter(Quiz.is_available, Quiz.objects.all())
        serializer = QuizListSerializer(available_quizzes, many=True)
        return Response(serializer.data)


class GetQuizDetailView(GenericAPIView):
    serializer_class = QuizDetailSerializer

    def get(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        serializer = QuizDetailSerializer(quiz)
        return Response(serializer.data)


class CreateQuizView(GenericAPIView):
    serializer_class = CreateQuizSerializer

    def post(self, request):
        quiz = CreateQuizSerializer(data=request.data)
        if quiz.is_valid():
            quiz.save()
        return Response(quiz.data, status=201)


class CreateQuestionView(GenericAPIView):
    serializer_class = CreateQuestionSerializer

    def post(self, request):
        question = CreateQuestionSerializer(data=request.data)
        if question.is_valid():
            question.save()
        return Response(question.data, status=201)
