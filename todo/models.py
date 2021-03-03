from django.db import models

# Create your models here.
class Tasks(models.Model):

    task = models.CharField(max_length=100,null=False, blank=False,primary_key=True)
    def __str__(self):
        return str(self.task)
