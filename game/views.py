from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Task, SubTask

class IndexView(generic.ListView):
    template = 'game/index.html'
    context_object_name = 'latest_task_list'

    def get_queryset(self):
        return Task.objects.order_by('-assign_date')[:5]

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'game/detail.html', {'task': task})

def subtasks(request, task_id):
  response = "You're looking at the subtask of task %s."
  return HttpResponse(response % task_id)

def join(request, task_id):
  return HttpResponse("You're ask for the task %s." % task_id)
