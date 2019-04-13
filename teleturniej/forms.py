from django import forms

class NickForm(forms.Form):
    your_name = forms.CharField(label='nick', max_length=100)

class Answer(forms.Form):
    answer =  forms.CharField(label='answer')   

