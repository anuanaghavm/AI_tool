from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    category = models.TextField()

    def __str__(self):
        return self.text

class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'M'),
        ('Female', 'F'),
        ('Other', 'O'),
    ]
    name = models.CharField(max_length=200)
    phone = models.TextField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    dob = models.DateField()
    email = models.EmailField()
    address = models.TextField()

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
    question = models.ForeignKey(Question, related_name='student_answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'question')
        ordering = ['-created_at']  # Order by most recent first

    def __str__(self):
        return f"{self.student.name} - {self.question.text}: {self.answer}"
