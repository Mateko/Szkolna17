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


def getting_question(request):
    level = request.session.get('level')

    try:
        random_dimension = random.randint(0, 3)   
        questions = q.objects.get(level=level)
        selected_question = question[random_dimension].question
        question = get_object_or_404(q, question=selected_question)    
        available_answers = a.objects.filter(question=available_questions)
        correct_answer = a.objects.filter(question_id=available_questions, is_correct_answer=1)[0].answer

    except (KeyError, q.DoesNotExist):
        return render(request, 'teleturniej/game.html', {
            'question': question,
            'error_message': 'Nie ma takiego pytania',
        })
    else:
        print(selected_question)
        request.session['question'] = selected_question
        request.session['first_answer'] = available_answers.first().answer
        request.session['second_answer'] = available_answers[1].answer
        request.session['third_answer'] = available_answers[2].answer
        request.session['four_answer'] = available_answers[3].answer
        request.session['correct_answer'] = correct_answer


def get_name(request):

    if request.method == 'POST':
        form = NickForm(request.POST)

        if form.is_valid():
            nick = form.cleaned_data['your_name']
            request.session['nick'] = nick
            request.session['level'] = 1
            request.session['call_chat'] = 1
            request.session['fifty_fifty'] = 1
            request.session['call_major'] = 1
            getting_question(request)
            return HttpResponseRedirect('game')
    else:
        form = NickForm()

    return render(request, 'teleturniej/index.html', {'form': form})


def game(request):
    nick = request.session.get('nick')
    level = request.session.get('level')
    ask_chat = request.session.get('call_chat')
    fifty_fifty = request.session.get('fifty_fifty')
    call_major = request.session.get('call_major')
    question = request.session.get('question')
    first_answer = request.session.get('first_answer')
    second_answer = request.session.get('second_answer')
    third_answer = request.session.get('third_answer')
    four_answer = request.session.get('four_answer')
    correct_answer = request.session.get('correct_answer')
    question_object = q.objects.get(question=question)

    return render(request, 'teleturniej/game.html', {
        'nick': nick, 'question': question, 'first_answer': first_answer, 
        'second_answer':  second_answer, 'third_answer': third_answer, 
        'four_answer': four_answer, 'level': level, 'ask_chat': ask_chat, 
        'fifty_fifty': fifty_fifty, 'call_major': call_major, 'correct_answer': correct_answer,
        'question_object': question_object        
    })

def level_result(request):
    nick = request.session.get('nick')
    pk_question = request.session.get('question')
    level = request.session.get('level')

    if request.method == 'POST':
        form = Answer(request.POST)

        if form.is_valid():
            current_answer = form.cleaned_data['answer']
            check_answer = a.objects.filter(answer=current_answer, is_correct_answer=1)

            if (check_answer.first() != None):
                request.session['level'] += 1
                getting_question(request)
                return render(request, 'teleturniej/level_result.html', {'nick': nick})   
            else:
                request.session['level'] = 1
                return render(request, 'teleturniej/level_result.html', {'nick':nick, 'level':level, 'game_end':'Niestety, to koniec twojej przygody!'})

        else:
            form = Answer()

        return render(request, 'teleturniej/index.html', {'form': form})

def life_preserver(request):

    if request.method == 'POST':
        form = LifePreserver(request.POST)
         
        if form.is_valid():
            life_preserver = form.cleaned_data['life_preserver']
            request.session['%s' % life_preserver] = 0 
    
        return HttpResponse(
            json.dumps(life_preserver),
            content_type="application/json"
        ) 
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

        
