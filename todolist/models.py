from django.db import models
from matplotlib.pyplot import title
from tables import Description
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,blank=True,null=True)
    Description=models.TextField(null=True,blank=True,)
    complete=models.BooleanField(default=False)
    creeated=models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return f'title :  {self.   title}'

    class Meta:
        ordering=['complete']