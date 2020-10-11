from django.db import models

# Create your models here.
class  ToDoList(models.Model):
    title = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.title