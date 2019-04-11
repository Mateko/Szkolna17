from django.contrib import admin

from .models import Question, Answers, CorrectAnswer
# Register your models here.

admin.site.register([Question, Answers, CorrectAnswer])


