from django.urls import path

from . import views

urlpatterns = [

    path("question/create", views.QuestionViewSet.as_view({"post": "create"}), name="question-create"),
    path("question/list", views.QuestionViewSet.as_view({"get": "list"}), name="question-list"),
    path("question/<int:pk>", views.QuestionViewSet.as_view({"get": "retrieve"}), name="question-retrieve"),
    path("question/update/<int:pk>", views.QuestionViewSet.as_view({"post": "partial_update"}), name="question-update"),
    path("question/delete/<int:pk>", views.QuestionViewSet.as_view({"delete": "destroy"}), name="question-delete"),

    path("quiz/create", views.QuizViewSet.as_view({"post": "create"}), name="quiz-create"),
    path("quiz/list", views.QuizViewSet.as_view({"get": "list"}), name="quiz-list"),
    path("quiz/retrieve/<int:pk>", views.QuizViewSet.as_view({"get": "retrieve"}), name="quiz-retrieve"),
    path("quiz/update/<int:pk>", views.QuizViewSet.as_view({"post": "partial_update"}), name="quiz-update"),
    path("quiz/delete/<int:pk>", views.QuizViewSet.as_view({"delete": "destroy"}), name="quiz-delete"),
    path("quiz/questions/<int:pk>", views.QuizViewSet.as_view({"get": "questions"}), name="quiz-questions"),
    path("quiz/list-of-available/", views.QuizViewSet.as_view({"get": "list_of_available"}), name="quiz-list-of-available"),

]
