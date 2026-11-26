from django.contrib import admin
from .models import Task, Contact


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'student_name', 'created_at')
    search_fields = ('task_name', 'student_name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_number', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
