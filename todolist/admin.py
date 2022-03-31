from django.contrib import admin
from .models import Task
# Register your models here.
admin.site.site_header='Kiash Admin panel'

admin.site.site_title='Kiash Admin panel'

admin.site.register(Task)