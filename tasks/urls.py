from django.urls import path
from tasks.views import create_task, view_tasks, task_search_feature, show_task


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", view_tasks, name="show_my_tasks"),
    path("tasksearch/", task_search_feature, name="task_search_feature"),
    path("<int:id>/", show_task, name="show_task"),
]
