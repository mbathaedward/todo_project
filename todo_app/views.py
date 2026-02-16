from django.shortcuts import render,get_object_or_404,redirect
from .models import Task
from .forms import TaskCreateform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import View,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.

    
class TaskListView(View):
   template_name = 'todo_app/list.html'

   def get(self, request):
     tasks = Task.objects.all().order_by('status')
     paginator = Paginator(tasks, 5, orphans=4, allow_empty_first_page=True)
     page = request.GET.get('page')

     try:
        paginated_tasks = paginator.page(page)
     except PageNotAnInteger:
        paginated_tasks = paginator.page(1)
     except EmptyPage:
        paginated_tasks = paginated_tasks.page(paginator.num_pages)

     context = {'tasks':paginated_tasks, 'title':'list tasks' }
   
     return render(request, self.template_name,context )
   
class TaskDetailView(DetailView):
   model = Task
   template_name = 'todo_app/detail.html'
   context_object_name = 'task'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = Task
      return context
   
class TaskCreateView(LoginRequiredMixin, CreateView):
   model = Task
   form = TaskCreateform
   template_name = 'todo_app/create.html'
   fields = ['title','description','status','due_date','author']
   success_url = 'list'

   def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      context['title'] = 'Create task'
      return context
   

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form = TaskCreateform
    fields = ['title','description','status','due_date','author']
    template_name = 'todo_app/update.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      context['title'] = 'Update task'
      return context
    
class TaskDeleteView(LoginRequiredMixin,DeleteView):
      model = Task
      template_name = 'todo_app/delete.html'
      success_url = '/'

      def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Delete task'
        return context

   



