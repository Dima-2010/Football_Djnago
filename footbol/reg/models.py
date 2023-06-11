from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    year = models.IntegerField(default=20, verbose_name='Год рождения ученика')
    student = models.CharField(max_length=56, verbose_name='Ф.И ученика')


    def __str__(self):
        return f'{self.student} {self.year}.г'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['year']
