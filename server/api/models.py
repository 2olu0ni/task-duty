from django.db import models

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length=30)
    description = models.TextField()
    tags = models.ForeignKey('Tags', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.task_title


class Tags(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name
        

        