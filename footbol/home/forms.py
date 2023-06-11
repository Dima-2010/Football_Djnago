from django import forms
from django.forms import TextInput, TimeInput, Select, SelectMultiple, FileInput, Textarea, DateInput

from home.models import table, month, news, forum, matches, match_res


class TableForm(forms.ModelForm):
    class Meta:
        model = table
        fields = ['title', 'description', 'data', 'student']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Название'
            }),
            "description": TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Место'
            }),

            "data": TimeInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Время',
                "type": "time"

            }),
            "student": SelectMultiple(attrs={
                'class': 'form-control article',
            }),
        }


class MonthForm(forms.ModelForm):
    class Meta:
        model = month
        fields = ['title']

        widgets = {
            'title': Select(attrs={
                'class': 'form-control'
            })
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = news
        fields = ['title', 'img', 'text', 'date', 'time']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Название'
            }),
            'img': FileInput(attrs={
                'class': 'form-control article btm btn-success',
                'style': 'visibility:hidden; width: 100%;',
                'id': 'files'
            }),
            'text': Textarea(attrs={
                'class': 'form-control article',
                'placeholder': 'Текст',
                'rows': 3
            }),
            'date': DateInput(attrs={
                'class': 'form-control article',
                'type': 'date'
            }),
            'time': TimeInput(attrs={
                'class': 'form-control',
                "type": "time"
            })
        }


class ForumForm(forms.ModelForm):
    class Meta:
        model = forum
        fields = ['text', 'img']

        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control article text',
                'placeholder': 'Написать сообщение...',

            }),
            'img': FileInput(attrs={
                'class': 'form-control article btm btn-success',
                'style': 'visibility:hidden; width: 100%;',
                'id': 'files'
            }),
        }


class MatchesForm(forms.ModelForm):
    class Meta:
        model = matches
        fields = ['place', 'date', 'time', 'student', 'color', 'commands']

        widgets = {
            'place': TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Место'
            }),
            'date': DateInput(attrs={
                'class': 'form-control article',
                'type': 'date'
            }),
            'time': TimeInput(attrs={
                'class': 'form-control',
                "type": "time"
            }),
            "student": SelectMultiple(attrs={
                'class': 'form-control article',
            }),
            'color': Select(attrs={
                'class': 'form-control',
                'label': 'Цвет формы'
            }),
            'commands': TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Команды'
            })
        }


class MatcheResForm(forms.ModelForm):
    class Meta:
        model = match_res
        fields = ['command_1', 'command_2', 'res']

        widgets = {
            'command_1': TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Первая команды'
            }),
            'command_2': TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Вторая команды'
            }),
            'res': TextInput(attrs={
                'class': 'form-control article',
                'placeholder': 'Счёт'
            })
        }