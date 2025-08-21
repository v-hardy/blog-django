from django.db import models

class Column(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    column = models.ForeignKey("tasks.Column", on_delete=models.CASCADE, related_name="tasks")
    order = models.PositiveIntegerField(default=0)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)   # se setea solo al crear
    updated_at = models.DateTimeField(auto_now=True)       # se actualiza cada vez que se guarda

    def __str__(self):
        return self.title
