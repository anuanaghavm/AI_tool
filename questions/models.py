from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=400,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
class Career(models.Model):
    category = models.ForeignKey(Category, related_name='careers', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    education_pathway = models.JSONField(null=True, blank=True)  # Change here
    score = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Stream(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.ForeignKey(Class, related_name='streams', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} ({self.class_name.name})"
    
class Question(models.Model):
    text = models.CharField(max_length=255)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=False)
    stream_name = models.ForeignKey(Stream, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text

