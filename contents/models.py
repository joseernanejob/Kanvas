from django.db import models
from django.shortcuts import get_object_or_404
from uuid import uuid4

from courses.models import Course

# Create your models here.


class Content(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    content = models.TextField()
    video_url = models.CharField(max_length=200, null=True)

    course = models.ForeignKey(
        "courses.Course", on_delete=models.PROTECT, related_name="contents"
    )
