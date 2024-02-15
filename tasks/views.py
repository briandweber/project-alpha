from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from tasks.forms import CreateTaskForm
from django.contrib.auth.decorators import login_required


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


@login_required
def view_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/task_list.html", context)


@login_required
def task_search_feature(request):
    if request.method == "POST":
        search_query = request.POST['search_query']
        tasks = Task.objects.filter(name__icontains=search_query)
        context = {
            "query": search_query,
            "tasks": tasks,
        }
        return render(request, "tasks/task_search_results.html", context)
    else:
        context = {
            "query": search_query,
        }
        return render(request, "tasks/task_search_results.html", context)

@login_required
def show_task(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        "task": task,
    }
    return render(request, "tasks/detail.html", context)
