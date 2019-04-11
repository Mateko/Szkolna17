from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Twoj_nick', max_length=10)