from django import forms
from .models import Student, ToDo

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add a new task...', 'style': 'padding: 1rem;'}),
            'priority': forms.Select(attrs={'style': 'padding: 1rem;'})
        }
