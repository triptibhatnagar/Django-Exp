from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    rollNo = models.IntegerField()
    skills = TaggableManager()

    def __str__(self):
        return self.name