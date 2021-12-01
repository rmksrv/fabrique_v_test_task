from django.contrib import admin
from .models import Quiz, Question, Answer


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = (
        QuestionInline,
    )
    list_display = (
        "name",
        "started_at",
        "finished_at"
    )
