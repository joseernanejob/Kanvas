from django.db import models
from uuid import uuid4

# Create your models here.


class Status(models.TextChoices):
    not_started = "not started"
    in_progress = "in progress"
    finished = "finished"


class Course(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        choices=Status.choices, default=Status.not_started, max_length=11
    )

    start_date = models.DateField()
    end_date = models.DateField()

    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.PROTECT,
        related_name="account",
        null=True,
        default=None,
    )

    students = models.ManyToManyField(
        "accounts.Account",
        through="students_courses.StudentCourse",
        related_name="courses",
    )
