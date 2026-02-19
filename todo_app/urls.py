from django.urls import path
from .views import TaskListView,TaskDetailView,TaskDeleteView,TaskUpdateView,TaskCreateView

#our urls goes here
urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
    path('create/', TaskCreateView.as_view(), name='create'),

    path('api/tasks', TaskListView.as_view(), name='api'),
     path('api-list/', TaskListView.as_view(), name='api-list')


]