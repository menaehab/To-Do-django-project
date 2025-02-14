from django.db import models


# Create your models here.
class Task(models.Model):
    task = models.CharField(null=True, max_length=250)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task
