from django import forms
from worksite.polls.models import Poll, Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ('poll',) 