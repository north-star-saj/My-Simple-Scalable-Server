# todo_list/todo_app/models.py
from django.db import models
from django.urls import reverse
from django.utils import timezone


def one_week_hence():
    """A thing"""
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    """A thing"""

    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        """A thing"""
        return reverse("list", args=[self.id])

    def __str__(self):
        """A thing"""
        return str(self.title)


class ToDoItem(models.Model):
    """A thing"""

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """A thing"""
        return reverse("item-update", args=[str(self.todo.id), str(self.id)])

    def __str__(self):
        """A thing"""
        return f"{self.title}: due {self.due_date}"

    class Meta:
        """A thing"""

        ordering = ["due_date"]
