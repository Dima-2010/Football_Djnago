from django.urls import path

from . import views
from .views import Logaut_user

urlpatterns = [
    path('registration', views.RegisterUser.as_view(), name='reg'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logaut', Logaut_user, name='logaut'),

]
