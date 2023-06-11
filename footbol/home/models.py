from django.db import models

from reg.models import CustomUser


class date(models.Model):
    date = models.IntegerField(verbose_name='Число', null=True, blank=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Дата'
        verbose_name_plural = 'Даты'


class month(models.Model):
    MONTH = [
        ("Январь", "Январь"),
        ("Февраль", "Февраль"),
        ("Март", "Март"),
        ("Апрель", "Апрель"),
        ("Май", "Май"),
        ("Июнь", "Июнь"),
        ("Июль", "Июль"),
        ("Август", "Август"),
        ("Сентябрь", "Сентябрь"),
        ("Октябрь", "Октябрь"),
        ("Ноябрь", "Ноябрь"),
        ("Декабрь", "Декабрь"),

    ]

    title = models.CharField(max_length=20, verbose_name="Месяц", choices=MONTH, default='Январь')


def __str__(self):
    return self.title


class Meta:
    verbose_name = 'месяц'
    verbose_name_plural = 'месяц'


class table(models.Model):
    date = models.ForeignKey(date, on_delete=models.CASCADE, verbose_name='Расписание', blank=True, null=True,
                             related_name='table_date')
    student = models.ManyToManyField(CustomUser, verbose_name='Ученик', blank=True, null=True,
                                     related_name='table_student')
    title = models.CharField(max_length=155)
    description = models.TextField(blank=True)
    data = models.TimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписания'


class news(models.Model):
    title = models.CharField(max_length=42, verbose_name='Название')
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    text = models.TextField()
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class forum(models.Model):
    text = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    auther = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Форум'
        verbose_name_plural = 'Форумы'


class matches(models.Model):
    COLOR = [
        ("Синяя", "Синяя"),
        ("Белая", "Белая")
    ]

    place = models.TextField()
    student = models.ManyToManyField(CustomUser, verbose_name='Ученик', blank=True, null=True,
                                     related_name='matches_student')
    date = models.DateField()
    time = models.TimeField()
    color = models.CharField(max_length=20, choices=COLOR, default='Синяя')
    commands = models.CharField(max_length=132, null=True, blank=True)

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'


class match_res(models.Model):
    command_1 = models.CharField(max_length=32)
    res = models.CharField(max_length=8)
    command_2 = models.CharField(max_length=32)

    def __str__(self):
        return self.command_1



