# models.py
from django.db import models

CONVERSION_CHOICES = [
    ('marks_to_percentage', 'Marks ➝ Percentage'),
    ('cgpa_to_percentage', 'CGPA ➝ Percentage'),
    ('Grade_to_percentage', 'Letter Grade ➝ Marks/Percentage'),
    ('board_specific', 'Board-Specific Conversion'),
]

class Conversion(models.Model):
    conversion_type = models.CharField(max_length=50, choices=CONVERSION_CHOICES)
    obtained_marks = models.FloatField(null=True, blank=True)
    total_marks = models.FloatField(null=True, blank=True)
    value = models.TextField(blank=True, null=True)  # For cgpa, letter grade etc.
    percentage = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 