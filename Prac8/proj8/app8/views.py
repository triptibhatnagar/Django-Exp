from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# List all students
def list_students(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Add new student
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# Edit student
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

# Delete student
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('list_students')
    return render(request, 'student_confirm_delete.html', {'student': student})