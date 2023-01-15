from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group_posts/<slug>/', views.group_posts),
]