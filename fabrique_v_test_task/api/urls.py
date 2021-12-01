from django.urls import path

from . import views

urlpatterns = [
    path("get-available-quizzes/", views.GetAvailableQuizzesView.as_view()),
    path("get-quiz-detail/<int:pk>", views.GetQuizDetailView.as_view()),
    path("create-quiz/", views.CreateQuizView.as_view()),
]
