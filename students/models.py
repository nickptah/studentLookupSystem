from django.db import models

class Student(models.Model):
    admission_no = models.CharField(max_length=40, unique=True, db_index=True)
    full_name = models.CharField(max_length=150)
    course_code = models.CharField(max_length=30)
    campus = models.CharField(max_length=80)
    supervisor = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['admission_no']

    def __str__(self):
        return f'{self.admission_no} - {self.full_name}'
