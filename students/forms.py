from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['admission_no', 'full_name', 'course_code', 'campus', 'supervisor']
        widgets = {field: forms.TextInput(attrs={'class': 'input'}) for field in fields}

class StudentSearchForm(forms.Form):
    admission_no = forms.CharField(max_length=40, label='Admission Number', widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'e.g. DCF-02-0248/2025', 'autocomplete': 'off'
    }))

class ExcelUploadForm(forms.Form):
    file = forms.FileField(label='Excel file', widget=forms.ClearableFileInput(attrs={'accept': '.xlsx'}))
    replace_existing = forms.BooleanField(required=False, initial=False, label='Update existing admission numbers')
