from django.db import models

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    blog = models.ForeignKey('blogs.Blog', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content} by {self.author}"
