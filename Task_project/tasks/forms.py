from django import forms
from .models import Task, Contact


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['student_name', 'task_name', 'description']
        widgets = {
            'student_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Your name'
            }),
            'task_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'TASK NAME'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'DESCRIPTION', 'rows': 4
            }),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'contact_number', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'FNAME'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'LNAME'
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Contact number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Email'
            }),
        }
