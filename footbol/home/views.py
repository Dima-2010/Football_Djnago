from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView, CreateView

from home.forms import TableForm, MonthForm, NewsForm, ForumForm, MatchesForm, MatcheResForm
from home.models import date, month, table, news, forum, matches, match_res


def home(request):
    data = {"date": date.objects.all(),
            "month": month.objects.all(),
            "matches": matches.objects.all().order_by('date'),
            "match_res": match_res.objects.all()
            }
    return render(request, 'home/home.html', data)


# def news_page(request):
#    data = {"news": news.objects.all()}
#    return render(request, 'home/news.html', data)


@login_required
def my_table(request):
    data = {"date": date.objects.all(),
            "month": month.objects.all(),
            "table": table.objects.filter(student=request.user).order_by("date"),
            "matches": matches.objects.all().filter(student=request.user).order_by("date"),
            }
    return render(request, 'home/my_table.html', data)


class news_page(CreateView, ListView):
    model = news
    template_name = 'home/news.html'
    form_class = NewsForm
    context_object_name = 'news'
    success_url = reverse_lazy('news')

    def __init__(self, *args, **kwargs):
        super(news_page, self).__init__(*args, **kwargs)
        self.object_list = self.get_queryset()


class details(DetailView, FormMixin):
    model = date
    template_name = 'home/details.html'
    context_object_name = 'date'
    form_class = TableForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('details', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object = None
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.date = self.get_object()
        self.object.save()
        return super().form_valid(form)


class table_update(UpdateView):
    model = table
    template_name = 'home/table_update.html'
    form_class = TableForm
    success_url = reverse_lazy('home')


class table_delete(DeleteView):
    model = table
    template_name = 'home/table_delete.html'
    context_object_name = 'table'
    success_url = reverse_lazy('home')


class month_update(UpdateView):
    model = month
    template_name = 'home/month_update.html'
    form_class = MonthForm
    success_url = reverse_lazy('home')


class news_delete(DeleteView):
    model = news
    template_name = 'home/table_delete.html'
    context_object_name = 'table'
    success_url = reverse_lazy('news')


class forum(CreateView, ListView):
    model = forum
    template_name = 'home/forum.html'
    context_object_name = 'forum'
    form_class = ForumForm
    success_url = reverse_lazy('forum')

    def __init__(self, *args, **kwargs):
        super(forum, self).__init__(*args, **kwargs)
        self.object_list = self.get_queryset()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.auther = self.request.user
        self.object.save()
        return super().form_valid(form)


class match_create(CreateView):
    model = matches
    template_name = 'home/create.html'
    form_class = MatchesForm
    success_url = reverse_lazy('home')


class match_update(UpdateView):
    model = matches
    template_name = 'home/create.html'
    form_class = MatchesForm
    success_url = reverse_lazy('home')


class match_delete(DeleteView):
    model = matches
    template_name = 'home/table_delete.html'
    context_object_name = 'table'
    success_url = reverse_lazy('home')


class Match_res(CreateView):
    model = match_res
    template_name = 'home/create.html'
    form_class = MatcheResForm
    success_url = '/'


class match_res_delete(DeleteView):
    model = match_res
    template_name = 'home/table_delete.html'
    context_object_name = 'table'
    success_url = reverse_lazy('home')