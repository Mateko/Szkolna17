from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, reverse
from .models import Question as q, Answers as a
from django.views import generic
from django.shortcuts import render
from .forms import NickForm, Answer, LifePreserver
import random
import math
import json

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NickForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #request.session['nick'] = form.your_name
            nick = form.cleaned_data['your_name']
            request.session['nick'] = nick
            request.session['level'] = 1
            request.session['Zapytaj Chat'] = 1
            request.session['50/50'] = 1
            request.session['Zadzwon do majora'] = 1
            return HttpResponseRedirect('game')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NickForm()

    return render(request, 'teleturniej/index.html', {'form': form})


def game(request):
    nick = request.session.get('nick')
    level = request.session.get('level')
    ask_chat = request.session.get('Zapytaj Chat')
    fifty_fifty = request.session.get('50/50')
    call_major = request.session.get('Zadzwon do majora')
            
    try:
        random_dimension = level * 4
        available_questions = random.randint(random_dimension -3, random_dimension)      
        question = get_object_or_404(q, pk=available_questions)
        selected_question = q.objects.get(pk=available_questions)
        available_answers = a.objects.filter(question=available_questions)

    except (KeyError, q.DoesNotExist):
        return render(request, 'teleturniej/game.html', {
            'question': question,
            'error_message': 'Nie ma takiego pytania',
        })

    else:
        return render(request, 'teleturniej/game.html', {
            'nick': nick, 'question': selected_question, 'first_answer': available_answers.first(), 
            'second_answer':  available_answers[1], 'third_answer': available_answers[2], 
            'four_answer': available_answers[3], 'level': level, 'ask_chat': ask_chat, 
            'fifty_fifty': fifty_fifty, 'call_major': call_major          
        })

def level_result(request):
    nick = request.session.get('nick')
    pk_question = request.session.get('question')
    level = request.session.get('level')

    if request.method == 'POST':
        form = Answer(request.POST)
        print(form)
        if form.is_valid():
            current_answer = form.cleaned_data['answer']
            check_answer = a.objects.filter(answer=current_answer, is_correct_answer=1)
            
            if (check_answer.first() != None):
                request.session['level'] += 1
                return render(request, 'teleturniej/level_result.html', {'nick': nick})   
            else:
                request.session['level'] = 1
                return render(request, 'teleturniej/level_result.html', {'nick':nick, 'level':level, 'game_end':'Niestety, to koniec twojej przygody!'})

        else:
            form = Answer()

        return render(request, 'teleturniej/index.html', {'form': form})

    if request.method == 'DELETE':
        print('a')
        return render(request, 'teleturniej/index.html', {'form': form})

def life_preserver(request):

    if request.method == 'POST':
        form = LifePreserver(request.POST)

   
        if form.is_valid():
            life_preserver = form.cleaned_data['life_preserver']
            request.session['%s' % life_preserver] = 0 
            print(life_preserver)
        return HttpResponse(
            json.dumps(life_preserver),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

        
