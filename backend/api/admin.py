"""Admin for tasks."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Task admin."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
