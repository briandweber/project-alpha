from django.shortcuts import render
from projects.models import Project

# Create your views here.
def list_projects(request):
    list_of_projects = Project.objects.all()
    context = {
        "list_of_projects": list_of_projects,
    }
    return render(request, "projects/projects.html", context)
