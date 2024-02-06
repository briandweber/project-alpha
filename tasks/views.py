from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import CreateTaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateTaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create_task.html", context)
