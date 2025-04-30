from rest_framework import serializers
from questions.serializers import StreamSerializer
from .models import Student,StudentAnswer,Personal,Education,StudentAssessment
from questions.models import Stream,Class,Question

class StudentAnswerSerializer(serializers.ModelSerializer):
    student_uuid = serializers.UUIDField(write_only=True)
    question_id = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), source='question', write_only=True)
    student_name = serializers.StringRelatedField(source='student.name', read_only=True)
    question_text = serializers.StringRelatedField(source='question.text', read_only=True)

    class Meta:
        model = StudentAnswer
        fields = ['id', 'student_uuid', 'question_id', 'answer_text', 'student_name', 'question_text', 'created_at']

    def create(self, validated_data):
        student_uuid = validated_data.pop('student_uuid')
        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Student with this UUID does not exist.")

        return StudentAnswer.objects.create(student=student, **validated_data)
    

class PersonalSerializer(serializers.ModelSerializer):
    student_uuid = serializers.UUIDField(write_only=True)
    student_name = serializers.CharField(source='student.name', read_only=True)

    class Meta:
        model = Personal
        fields = ['id', 'student_uuid','student_name', 'hobbies', 'curicular_activities', 'achievements', 'internship_projects', 'languages_known']

    def create(self, validated_data):
        student_uuid = validated_data.pop('student_uuid')
        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Student with this UUID does not exist.")

        return Personal.objects.create(student=student, **validated_data)


class EducationSerializer(serializers.ModelSerializer):
    student_uuid = serializers.UUIDField(write_only=True)
    student_name = serializers.CharField(source='student.name', read_only=True)

    class Meta:
        model = Education
        fields = ['id', 'student_uuid', 'studying_in','student_name', 'specification', 'college', 'course', 'passing_year', 'university', 'planning_to_study', 'preparing_for_entrance_exam']

    def create(self, validated_data):
        student_uuid = validated_data.pop('student_uuid')
        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Student with this UUID does not exist.")

        return Education.objects.create(student=student, **validated_data)


class StudentSerializer(serializers.ModelSerializer):
    personal_details = PersonalSerializer(read_only=True)
    education_details = EducationSerializer(read_only=True)
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), source='class_name', write_only=True)
    stream_id = serializers.PrimaryKeyRelatedField(queryset=Stream.objects.all(), source='stream_name', write_only=True)
    class_name = serializers.SerializerMethodField()
    stream_name = StreamSerializer(read_only=True)
    answers = StudentAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = [
            'id', 'student_uuid','name', 'phone', 'gender', 'dob', 'email', 'address',
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
    

    def validate(self, data):
        class_instance = data.get('class_name')
        stream_instance = data.get('stream_name')

        if stream_instance.class_name != class_instance:
            raise serializers.ValidationError("Selected stream does not belong to the selected class.")
        return data

class StudentAssessmentSerializer(serializers.ModelSerializer):
    student_uuid = serializers.UUIDField(write_only=True)

    class Meta:
        model = StudentAssessment
        fields = ['id', 'student_uuid', 'assessment_done']

    def create(self, validated_data):
        student_uuid = validated_data.pop('student_uuid')
        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Student with this UUID does not exist.")

        confirmation = StudentAssessment.objects.create(student=student, **validated_data)

        if confirmation.assessment_done:
            student.assessment_count += 1
            student.save()

        return confirmation