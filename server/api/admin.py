from django.contrib import admin
from .models import Task, Tags

# Register your models here.

admin.site.register(Task)
admin.site.register(Tags)
