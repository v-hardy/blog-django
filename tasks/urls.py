from django.urls import path
from . import views

urlpatterns = [
    path("", views.board, name="board"),
    path("add-task/<int:column_id>/", views.add_task, name="add_task"),
    path("move-task/<int:task_id>/<int:column_id>/", views.move_task, name="move_task"),
]
