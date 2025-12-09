from django.urls import path
from . import views
from .api_views import StudentListAPI, StudentDetailAPI

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('students/', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    
    # ToDo
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/toggle/<int:id>/', views.toggle_todo, name='toggle_todo'),
    path('todos/delete/<int:id>/', views.delete_todo, name='delete_todo'),

    # API
    path('api/students/', StudentListAPI.as_view(), name='students_api'),
    path('api/students/<int:pk>/', StudentDetailAPI.as_view(), name='student_api'),
]
