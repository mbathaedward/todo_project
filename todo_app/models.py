from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return f"Title: {self.title}\n description:{self.description}"