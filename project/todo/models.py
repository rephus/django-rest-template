import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel

class Task(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default=None, null=True, blank=True)
    completed = models.BooleanField(default=False)
    due = models.DateTimeField(default=None, blank=True, null=True)
