from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Student, ToDo
from .forms import StudentForm, ToDoForm

def home(request):
    return render(request, 'students/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def about(request):
    return render(request, 'students/about.html')

def contact(request):
    return render(request, 'students/contact.html')

def list_students(request):
    search_query = request.GET.get('search')
    if search_query:
        students = Student.objects.filter(
            Q(name__icontains=search_query) |
            Q(department__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    else:
        students = Student.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

@login_required
def update_student(request, id):
    student = get_object_or_404(Student, pk=id)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('list_students')
    return render(request, 'students/update_student.html', {'form': form})

@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'students/confirm_delete.html', {'student': student})


@login_required
def todo_list(request):
    todos = ToDo.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = ToDoForm()
    return render(request, 'students/todo_list.html', {'todos': todos, 'form': form})

@login_required
def toggle_todo(request, id):
    todo = get_object_or_404(ToDo, pk=id, user=request.user)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('todo_list')

@login_required
def delete_todo(request, id):
    todo = get_object_or_404(ToDo, pk=id, user=request.user)
    todo.delete()
    return redirect('todo_list')
