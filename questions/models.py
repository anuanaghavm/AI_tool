from django.db import models

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES)

    def __str__(self):
        return self.text
