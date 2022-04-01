from django.urls import path
from .views import Customlogin, TaskDelete, TaskDetail, TaskView,TaskCreate,TaskUpadte,Registerform
from  django.contrib.auth.views import LogoutView


app_name='todolist'
urlpatterns = [
    path('login/',Customlogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='todolist:login'),name='logout'),
    path('register/',Registerform.as_view(),name='register'),
    path('',TaskView.as_view(),name='task'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task-detail'),
    path('create/',TaskCreate.as_view(),name='task-create'),
    path('update/<int:pk>/',TaskUpadte.as_view(),name='task-update'),
    path('delete/<int:pk>/',TaskDelete.as_view(),name='task-delete')
]
