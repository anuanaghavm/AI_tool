from rest_framework import serializers
from questions.serializers import StreamSerializer
from .models import Student,StudentAnswer,Personal,Education
from questions.models import Stream,Class,Question

class StudentAnswerSerializer(serializers.ModelSerializer):
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)
    question_id = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), source='question', write_only=True)
    student_name = serializers.StringRelatedField(source='student.name', read_only=True)
    question_text = serializers.StringRelatedField(source='question.text', read_only=True)

    class Meta:
        model = StudentAnswer
        fields = ['id', 'student_id', 'question_id', 'answer_text', 'student_name', 'question_text', 'created_at']

    def create(self, validated_data):
        # Create an answer for the given student and question
        return StudentAnswer.objects.create(**validated_data)

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
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), source='class_name', write_only=True)
    stream_id = serializers.PrimaryKeyRelatedField(queryset=Stream.objects.all(), source='stream_name', write_only=True)
    class_name = serializers.SerializerMethodField()
    stream_name = StreamSerializer(read_only=True)
    answers = StudentAnswerSerializer(many=True, read_only=True)
    assessment_count = serializers.SerializerMethodField()  # 👈 add this line

    class Meta:
        model = Student
        fields = [
            'id', 'name', 'phone', 'gender', 'dob', 'email', 'address',
            'personal_details', 'education_details',
            'class_id', 'stream_id',
            'class_name', 'stream_name',
            'answers', 'assessment_count'  
        ]

    def get_class_name(self, obj):
        return {
            'id': obj.class_name.id,
            'name': obj.class_name.name
        }
    
    def get_assessment_count(self, obj):
        total_answers = obj.answers.count()
        if total_answers == 0:
            return 0
        assessments = total_answers // 20  
        return assessments

    def validate(self, data):
        class_instance = data.get('class_name')
        stream_instance = data.get('stream_name')

        if stream_instance.class_name != class_instance:
            raise serializers.ValidationError("Selected stream does not belong to the selected class.")
        return data
