from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):
    manager = models.ForeignKey(User,on_delete = models.CASCADE,default=None)
    title = models.CharField(max_length=500,default='no title')
    task = models.CharField(max_length=5000)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " - " + str(self.done)
    