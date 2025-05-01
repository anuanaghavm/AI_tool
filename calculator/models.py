import uuid
from django.db import models
from students.models import Student
import uuid

GRADE_TO_MARKS = {
    'A+': 95,
    'A': 90,
    'B+': 85,
    'B': 80,
    'C': 70,
    'D': 60,
    'F': 0,
}

class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    marks = models.FloatField(null=True, blank=True)
    grade = models.CharField(max_length=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.grade and not self.marks:
            self.marks = GRADE_TO_MARKS.get(self.grade.upper(), 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.student.name}"

class Percentage(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.student.name} - {self.percentage}%"
