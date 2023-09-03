from django.db import models
from uuid import uuid4

# Create your models here.


class Status(models.TextChoices):
    pending = "pending"
    accepted = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    status = models.CharField(
        choices=Status.choices, default=Status.pending, max_length=11
    )

    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="students_courses"
    )

    student = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="students_courses"
    )
