from django import forms
from worksite.polls.models import Poll, Choice

class PollForm(forms.ModelForm):
    class Meta:
		title = forms.CharField()
		pub_date = forms.DateField()

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ('poll',) 