from django.db import models
from django.urls import reverse


class Task(models.Model):

    title = models.CharField(max_length=200, help_text="Enter task title")
    description = models.TextField(blank=True, help_text="Optional task description")
    completed = models.BooleanField(default=False, help_text="Mark as completed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Show newest tasks first

    def __str__(self):
        """String representation of the task"""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a particular task"""
        return reverse('task_detail', args=[str(self.id)])