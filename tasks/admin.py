from django.contrib import admin
from tasks.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('user', 'title', 'is_completed', 'created_at')
    list_filter = ('user', 'is_completed')
    search_fields = ['title', 'description', 'user__username']

admin.site.register(Task , TaskAdmin)