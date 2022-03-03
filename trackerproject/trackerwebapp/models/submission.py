from django.db import models

from trackerwebapp.models.exercise import Exercise
from .classroom import Classroom
from .student import Student
from .exercise import Exercise

class Submission(models.Model):

    time_submitted = models.DateTimeField()
    exercise = models.ForeignKey(
        'Exercise', 
        null=False, 
        blank=False, 
        on_delete=models.CASCADE,
        default=1
    )
    student = models.ForeignKey(
        Student,
        related_name='submissions',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
