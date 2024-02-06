from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.

def list_projects(request):
    list_of_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_of_projects": list_of_projects
    }
    return render(request, "projects/projects.html", context)
