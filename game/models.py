import datetime

from django.db import models
from django.utils import timezone

class Task(models.Model):
    task_description = models.CharField(max_length=200)
    code_coins = models.IntegerField(default=0, null=True, blank=True)
    assign_date = models.DateTimeField('assignment date', null=True, blank=True)
    finish_date = models.DateTimeField('finish date', null=True, blank=True)
    def __str__(self):
      return self.task_description
    def was_assign_recently(self):
      return self.assign_date >= timezone.now() - datetime.timedelta(days=1)

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    sub_task_description = models.CharField(max_length=200)
    def __str__(self):
      return self.sub_task_description
