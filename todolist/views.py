from re import search, template
from attr import fields
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from matplotlib.style import context
from todolist.models import Task
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView,FormView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin
class Customlogin(LoginView):
    fields='__all__'
    redirect_authenticated_user=True
    def  get_success_url(self):
        return reverse_lazy('todolist:task')


class Registerform(FormView):
    template_name='register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('todolist:task')


    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)


        return super(Registerform,self).form_valid(form)

    def get(self,*args, **kwargs):
            if self.request.user.is_authenticated:
                return redirect('todolist:task')
            return super(Registerform,self).get(*args,**kwargs)




class TaskView(LoginRequiredMixin,ListView):
    model=Task 
    context_object_name='task'
    def get_context_data(self ,**kwargs):
        context=super().get_context_data(**kwargs)
        context['task']=context['task'].filter(user=self.request.user)
        context['countr']=context['task'].filter(complete=False).count()

        search_input=self.request.GET.get('search-area') 
        if search_input:
            context['task']=context['task'].filter(title__startswith=search_input)
            context['task']=search_input
        return context 

class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task  
    context_obeject_name='todolist:task'
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('todolist:task')
class TaskUpadte(LoginRequiredMixin,UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('todolist:task')


class TaskDelete(LoginRequiredMixin ,DeleteView):
    model=Task

    success_url=reverse_lazy('todolist:task')