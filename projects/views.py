from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import CreateProjectForm


@login_required
def list_projects(request):
    list_of_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_of_projects": list_of_projects
    }
    return render(request, "projects/projects.html", context)


@login_required
def show_project(request, id):
    proj = get_object_or_404(Project, id=id)
    context = {
        "proj": proj,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(False)
            new_project.owner = request.user
            new_project = form.save()
            return redirect("home")
    else:
        form = CreateProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create_project.html", context)
