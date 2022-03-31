from attr import fields
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from matplotlib.style import context
from todolist.models import Task
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView 

from django.contrib.auth.mixins import LoginRequiredMixin
class Customlogin(LoginView):
    fields='__all__'
    redirect_authenticated_user=True
    def  get_success_url(self):
        return reverse_lazy('tasks')




class TaskView(LoginRequiredMixin,ListView):
    model=Task 
    context_object_name='tasks'
    def get_context_data(self ,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['countr']=context['tasks'].filter(complete=False).count()
        return context 





class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task  
    context_obeject_name='todolist:task'
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('todolist:tasks')
class TaskUpadte(LoginRequiredMixin,UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('todolist:tasks')


class TaskDelete(LoginRequiredMixin ,DeleteView):
    model=Task

    success_url=reverse_lazy('todolist:tasks')