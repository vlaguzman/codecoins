from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('task/<int:task_id>/', views.detail, name='detail'),
  path('task/<int:task_id>/subtasks/', views.subtasks, name='subtasks'),
  path('task/<int:task_id>/join/', views.join, name='join'),
]
