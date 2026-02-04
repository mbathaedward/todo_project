from django.urls import path
from .views import task_list,task_detail,task_create,task_update,task_delete

#our urls goes here
urlpatterns = [
    path('', task_list, name='list'),
    path('detail/<int:id>/', task_update, name='update'),
    path('update/<int:id>/', task_detail, name='detail'),
    path('delete/<int:id>/', task_delete, name='delete'),
    path('create/', task_create, name='create'),

]