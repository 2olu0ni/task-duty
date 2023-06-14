
from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_Routes),
    path('tasks/', views.all_tasks),
    path('tasks/create/', views.create_task),
    path('tasks/<str:pk>/', views.single_task)
]