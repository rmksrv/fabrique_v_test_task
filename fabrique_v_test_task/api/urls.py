from django.urls import path

from . import views

urlpatterns = [
    path("quiz/available-quizzes/", views.GetAvailableQuizzesView.as_view()),
    path("quiz/detail/<int:pk>", views.GetQuizDetailView.as_view()),
    path("quiz/create", views.CreateQuizView.as_view()),
    path("question/add", views.CreateQuestionView.as_view()),
]
