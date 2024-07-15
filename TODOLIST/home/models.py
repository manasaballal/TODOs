from django.db import models


# Create your models here.
class Task(models.Model):
    TASKTITLE = models.CharField(max_length=30)
    TASKDESC = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.TASKTITLE
    


