from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import CreateProjectForm


@login_required
def list_projects(request):
    list_of_projects = Project.objects.filter(owner=request.user)
    context = {"list_of_projects": list_of_projects}
    return render(request, "projects/projects.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project,
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
            return redirect("list_projects")
    else:
        form = CreateProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create_project.html", context)


@login_required
def project_search_feature(request):
    if request.method == "POST":
        search_query = request.POST['search_query']
        projects = Project.objects.filter(name__icontains=search_query)
        context = {
            "query": search_query,
            "projects": projects
        }
        return render(request, "projects/project_search_results.html", context)
    else:
        context = {
            "query": search_query,
        }
        return render(request, "projects/project_search_results.html", context)
