from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import *

from reg.models import CustomUser




class CustomUserCreationForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Имя пользователя'}))
    student = CharField(widget=TextInput(attrs={'placeholder': 'Фамилия и имя ученика'}))
    password1 = CharField(widget=PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = CharField(widget=PasswordInput(attrs={'placeholder': 'Повтор пароля'}))
    year = CharField(widget=NumberInput(attrs={'placeholder': "Год рождения ученика"}))

    class Meta:
        model = CustomUser
        fields = ['student', 'password1', 'password2', 'year', 'username']


class UserLoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Имя пользователя'}))
    password = CharField(widget=PasswordInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
