from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group_list/<slug>/', views.group_list, name='group_list'),
]