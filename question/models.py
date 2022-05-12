from django.db import models


class Questionnaire(models.Model):
    name = models.CharField(max_length=155,)


class Question(models.Model):
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    text_question = models.CharField(max_length=255)


class Guest(models.Model):
    username = models.CharField(max_length=255,)


class QuestionGuestSession(models.Model):
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
    )
    guest = models.ForeignKey(
        Guest,
        on_delete=models.CASCADE,
        related_name='guest_sessions',
    )
    started_time = models.DateTimeField()

    class Meta:
        unique_together = ('questionnaire', 'guest',)


class AnswerRecord(models.Model):
    session = models.ForeignKey(
        QuestionGuestSession,
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    text_answer = models.CharField(max_length=255,)
    submitted_time = models.DateTimeField() #end time of each question

    class Meta:
        unique_together = ('session', 'question',)


