from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=30)

    def __str__(self):
        return self.question


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=30)

    def __str__(self):
        return self.answer

class CorrectAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)

    def __int__(self):
        return self.answer