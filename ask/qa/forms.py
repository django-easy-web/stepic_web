from .models import Answer, Question, User
from django import forms


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super(AskForm, self).clean()

    def save(self):
        self.cleaned_data['author'] = self._user
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def clean(self):
        cleaned_data = super(AnswerForm, self).clean()

    def save(self):
        self.cleaned_data['author'] = self._user
        return Answer.objects.create(**self.cleaned_data)