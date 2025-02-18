from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    description= models.TextField()
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} - {self.completed} -{self.user}"
    
