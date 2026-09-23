from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_no', 'full_name', 'course_code', 'campus', 'supervisor', 'updated_at')
    search_fields = ('admission_no', 'full_name', 'course_code', 'campus', 'supervisor')
    list_filter = ('course_code', 'campus')
    ordering = ('admission_no',)
