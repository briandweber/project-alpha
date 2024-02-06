from django.urls import path
from projects.views import list_projects


urlpatterns = [
    path("projects", list_projects, name="home"),
]
