from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from reg.forms import CustomUserCreationForm, UserLoginForm


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'reg/reg.html'
    success_url = reverse_lazy('login')




class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'reg/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def Logaut_user(request):
    logout(request)
    return redirect('login')
