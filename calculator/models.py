from django.db import models

GRADE_TO_MARKS = {
    'A+': 100,
    'A': 95, 
    'B+': 85,
    'B': 80,
    'C': 70,
    'D': 60,
    'F': 50,
}

class Subject(models.Model):
    name = models.CharField(max_length=100)
    obtained_marks = models.FloatField(null=True, blank=True)
    total_marks = models.FloatField(null=True, blank=True)
    marks = models.FloatField(null=True, blank=True)
    grade = models.CharField(max_length=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.obtained_marks is not None and self.total_marks is not None:
            self.marks = (self.obtained_marks / self.total_marks) * 100
        elif self.grade and not self.marks:
            self.marks = GRADE_TO_MARKS.get(self.grade.upper(), 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.marks} marks"

class Percentage(models.Model):
    percentage = models.FloatField()

    def __str__(self):
        return f"Percentage: {self.percentage}%"