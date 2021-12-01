from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Quiz
from .serializers import GetQuizListSerializer, GetQuizDetailSerializer, CreateQuizSerializer


class GetAvailableQuizzesView(GenericAPIView):
    serializer_class = GetQuizListSerializer

    def get(self, request):
        available_quizzes = filter(Quiz.is_available, Quiz.objects.all())
        serializer = GetQuizListSerializer(available_quizzes, many=True)
        return Response(serializer.data)


class GetQuizDetailView(GenericAPIView):
    serializer_class = GetQuizDetailSerializer

    def get(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        serializer = GetQuizDetailSerializer(quiz)
        return Response(serializer.data)


class CreateQuizView(GenericAPIView):
    serializer_class = CreateQuizSerializer

    def post(self, request):
        quiz = CreateQuizSerializer(data=request.data)
        if quiz.is_valid():
            quiz.save()
        return Response(status=201)
