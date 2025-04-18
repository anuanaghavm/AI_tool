from rest_framework import serializers
from .models import Question, Student, StudentAnswer, Personal ,Education

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class StudentAnswerSerializer(serializers.ModelSerializer):
    question_name = serializers.CharField(source='Question.text', read_only=True)
    class Meta:
        model = StudentAnswer
        fields = ['student','question','question_name','answer']

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    personal_details = PersonalSerializer(read_only=True)
    education_details = EducationSerializer(read_only=True)
    answers = StudentAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id','name', 'phone', 'gender', 'dob', 'email', 'address', 'personal_details', 'education_details', 'answers']
