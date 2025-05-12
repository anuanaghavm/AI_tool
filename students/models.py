from django.db import models
from questions.models import Class,Stream,Question
import uuid


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'M'),
        ('Female', 'F'),
        ('Other', 'O'),
    ]
    student_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  
    name = models.CharField(max_length=200)
    phone = models.TextField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    dob = models.DateField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    class_name = models.ForeignKey(Class, related_name='student', on_delete=models.CASCADE)
    stream_name = models.ForeignKey(Stream, related_name='student', on_delete=models.CASCADE)
    assessment_count = models.IntegerField(default=0)
    is_subscribed = models.BooleanField(default=False)
    firebase_user_id = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Personal(models.Model):
    student = models.OneToOneField(Student, related_name='personal_details', on_delete=models.CASCADE)
    hobbies = models.TextField()
    curicular_activities = models.TextField()
    achievements = models.TextField()
    internship_projects = models.TextField()
    languages_known = models.TextField()

    def __str__(self):
        return self.hobbies
    
class Education(models.Model):
    student = models.OneToOneField(Student, related_name='education_details', on_delete=models.CASCADE)
    studying_in = models.TextField()
    specification = models.TextField()
    college = models.TextField()
    course = models.TextField()
    passing_year = models.TextField()
    university = models.TextField()
    planning_to_study = models.BooleanField()
    preparing_for_entrance_exam = models.BooleanField()

    def __str__(self):
        return self.studying_in

class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField()  # Field to store the student's answer
    created_at = models.DateTimeField(auto_now_add=True)  # Time when the answer was submitted

    def __str__(self):
        return f"Answer by {self.student.name} for question {self.question.text[:50]}"

class StudentAssessment(models.Model):
    student = models.ForeignKey(Student, related_name='confirmations', on_delete=models.CASCADE)
    assessment_done = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.student.name} - {'Assessment Done' if self.assessment_done else 'Not Done'}"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    summary = models.JSONField() 
    aptitude_test = models.JSONField()  # For testName, completedAt, overallScore, etc.
    personality_test = models.JSONField()   # For individual category scores

    def __str__(self):
        return f"{self.student} - {self.summary.get('testName', '')}"
