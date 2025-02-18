from django.db import models
class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    description= models.TextField()
    title = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.title} - {self.completed}"
    
