from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)

    # class CategoryChoices(models.TextChoices):
    #     TECH = 'TECH', 'Technology'
    #     FOOD = 'FOOD', 'Food'
    #     SPORTS = 'SPORTS', 'Sports'
    #     MUSIC = 'MUSIC', 'Music'
    #     POLITICS = 'POLITICS', 'Politics'
    #     OTHER = 'OTHER', 'Other'

    # class TagsChoices(models.TextChoices):
    #     TAG1 = 'TAG1', 'Tag1'
    #     TAG2 = 'TAG2', 'Tag2'
    #     TAG3 = 'TAG3', 'Tag3'
    #     TAG4 = 'TAG4', 'Tag4'
    # category = models.CharField(
    #     max_length=20, 
    #     choices=CategoryChoices.choices, 
    #     default=CategoryChoices.OTHER
    #     )
    def __str__(self):
        return f"{self.title} by {self.author}"
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tags')

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
class Tags(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"