from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() # fetches the currently active user model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Each post linked to a user
    # CASCADE means: deleting user deletes all their posts
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title