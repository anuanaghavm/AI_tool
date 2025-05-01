from rest_framework import serializers
from .models import  Subject, Percentage
from students.models import Student
from students.serializers import StudentSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'marks', 'grade']


class SubjectBulkCreateSerializer(serializers.Serializer):
    student_uuid = serializers.UUIDField()
    subjects = SubjectSerializer(many=True)

    def create(self, validated_data):
        from students.models import Student
        student_uuid = validated_data.get('student_uuid')
        subjects_data = validated_data.get('subjects')

        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Invalid student UUID")

        subjects = []
        for subject_data in subjects_data:
            subject = Subject(student=student, **subject_data)
            subject.save()
            subjects.append(subject)

        return subjects


class PercentageSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)

    class Meta:
        model = Percentage
        fields = ['student_name', 'percentage']
