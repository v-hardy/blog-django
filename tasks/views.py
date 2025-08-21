from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task, Column

def board(request):
    columns = Column.objects.prefetch_related("tasks").order_by("order")
    return render(request, "tasks/board.html", {
        "columns": columns,
        "all_columns": columns,  # pasamos todas para usarlas en los templates
    })

def add_task(request, column_id):
    column = get_object_or_404(Column, id=column_id)
    title = request.POST.get("title")
    if title:
        Task.objects.create(title=title, column=column, order=column.tasks.count())
    return render(request, "tasks/task_list.html", {"column": column})

def move_task(request, task_id, column_id):
    task = get_object_or_404(Task, id=task_id)
    column = get_object_or_404(Column, id=column_id)
    task.column = column
    task.order = column.tasks.count()
    task.save()
    return render(request, "tasks/task_list.html", {"column": column})
