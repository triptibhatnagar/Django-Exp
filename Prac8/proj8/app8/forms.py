from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    # Meta = configuration for your ModelForm
    class Meta:
        model = Student
        fields = '__all__'  # Include all fields of the model