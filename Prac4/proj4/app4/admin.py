from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.register(Student)

admin.site.site_header = "Student management administration"
admin.site.site_title = "Student Management portal"
admin.site.index_title = "Welcome to student management admin"