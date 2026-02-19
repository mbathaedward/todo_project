from django.db import models
from django.db.models.signals import post_save,pre_save

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
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return f"Title: {self.title}\n description:{self.description}"
    
#Sender && Receiver
def save_task(sender, instance, **kwargs):
    print("signal received")
post_save.connect(save_task, sender=Task)
pre_save.connect(save_task, sender=Author)