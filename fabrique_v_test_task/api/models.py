import datetime

from django.conf import settings
from django.db import models
from django.utils.timezone import utc

from .constants import ANSWER_TYPE_CHOICES


class Quiz(models.Model):
    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    name = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")
    started_at = models.DateTimeField(verbose_name="Дата начала", auto_now_add=True, editable=False)
    finished_at = models.DateTimeField(verbose_name="Дата окончания", null=True)

    def questions(self):
        return Question.objects.filter(quiz=self)

    def is_available(self):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        return now < self.finished_at


class Question(models.Model):
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")
    answer_type = models.IntegerField(verbose_name="Тип ответа", choices=ANSWER_TYPE_CHOICES)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
