from __future__ import unicode_literals
from django.db import models
import os

# Create your models here.
class Question(models.Model):
  
    LEVELS = (
        (1, 'pierwszy_poziom'),
        (2, 'drugi_poziom'),
        (3, 'trzeci_poziom'),
        (4, 'czwarty_poziom'),
        (5, 'piaty_poziom'),
        (6, 'szosty_poziom'),
        (7, 'siodmy_poziom'),
        (8, 'osmy_poziom'),
        (9, 'dziewiaty_poziom'),
        (10, 'dziesiaty_poziom'),
        (11, 'jedenasty_poziom'),
        (12, 'dwunasty_poziom'),
    )
  
    question = models.CharField(max_length=64)
    level = models.IntegerField(choices=LEVELS)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.question

    def __int__(self):
        return self.level


class Answers(models.Model):   
    IS_CORRECT = (
        (1,'poprawna_odpowiedz'),
        (0, 'bledna_odpowiedz')
    )

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=30)
    is_correct_answer = models.IntegerField(choices=IS_CORRECT)

    def __str__(self):
        return self.answer

    def __int__(self):
        return self.is_correct_answer
