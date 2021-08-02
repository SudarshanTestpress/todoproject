from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = "tasks"

urlpatterns = [
    path("", views.AllTaskOverdueListView.as_view(), name="all_overdue_tasks"),
    path("taskssearch/", views.TaskFilterView.as_view(), name="task_search"),
    path("projects/", views.ProjectList.as_view(), name="create_and_list_project"),
    path("projects/create", views.ProjectCreateView.as_view(), name="create_project"),
    path("projects/<str:pk>", views.TaskListView.as_view(), name="list_task"),
    path(
        "projects/<str:pk>/updatename",
        views.ProjectUpdateView.as_view(),
        name="update_project",
    ),
    path(
        "projects/<str:pk>/deletename",
        views.ProjectDeleteView.as_view(),
        name="delete_project",
    ),
    path(
        "projects/<str:pk>/tasks/create",
        views.TaskCreateView.as_view(),
        name="create_task",
    ),
    path(
        "projects/<str:pk>/tasks/<str:task_pk>/update",
        views.TaskUpdateView.as_view(),
        name="update_task",
    ),
    path(
        "projects/<str:pk>/tasks/<str:task_pk>/delete",
        views.TaskDeleteView.as_view(),
        name="delete_task",
    ),
    path(
        "projects/<str:pk>/overduetasks",
        views.TaskOverdueListView.as_view(),
        name="list_overdue_tasks",
    ),
]
