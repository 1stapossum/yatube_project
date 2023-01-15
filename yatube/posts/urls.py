from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group_list/<slug>/', views.group_list),
]