from django import forms

class NickForm(forms.Form):
    your_name = forms.CharField(label='', max_length=100)

class Answer(forms.Form):
    answer = forms.CharField(label='')   

class LifePreserver(forms.Form):
    life_preserver = forms.CharField(label='')   

