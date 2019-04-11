from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, reverse
from .models import Question, Answers, CorrectAnswer
from django.views import generic
from django.shortcuts import render


def index(request):
    return render(request, 'teleturniej/index.html')