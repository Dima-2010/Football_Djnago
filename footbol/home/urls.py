from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/details', views.details.as_view(), name='details'),
    path('<int:pk>/table_update', views.table_update.as_view(), name='table_update'),
    path('<int:pk>/month_update', views.month_update.as_view(), name='month_update'),
    path('<int:pk>/table_delete', views.table_delete.as_view(), name='table_delete'),
    path('my_table', views.my_table, name='my_table'),
    path('news', views.news_page.as_view(), name='news'),
    path('<int:pk>/news_delete', views.news_delete.as_view(), name='news_delete'),
    path('forum', views.forum.as_view(), name='forum'),
    path('match_create', views.match_create.as_view(), name='match_create'),
    path('<int:pk>/match_update', views.match_update.as_view(), name='match_update'),
    path('<int:pk>/match_delete', views.match_delete.as_view(), name='match_delete'),
    path('match_res', views.Match_res.as_view(), name='match_res'),
    path('<int:pk>/match_res_delete', views.match_res_delete.as_view(), name='match_res_delete'),

]
