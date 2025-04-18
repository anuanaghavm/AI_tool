from rest_framework import serializers
from .models import Question, Student, StudentAnswer, Personal ,Education

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class StudentAnswerSerializer(serializers.ModelSerializer):
    question_text = serializers.SerializerMethodField()
    question_category = serializers.SerializerMethodField()
    
    class Meta:
        model = StudentAnswer
        fields = ['id', 'student', 'question', 'question_text', 'question_category', 'answer']
    
    def get_question_text(self, obj):
        return obj.question.text if obj.question else None
    
    def get_question_category(self, obj):
        return obj.question.category if obj.question else None

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
