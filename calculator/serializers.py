from rest_framework import serializers
from .models import Subject, Percentage

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'obtained_marks', 'total_marks', 'marks', 'grade']

class PercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percentage
        fields = ['percentage']