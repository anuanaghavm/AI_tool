from rest_framework import serializers
from .models import Question, Student, StudentAnswer, Personal ,Education,Class,Stream,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class StreamSerializer(serializers.ModelSerializer):
    class_name = serializers.StringRelatedField()
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(),source='class_name',write_only=True)

    class Meta:
        model = Stream
        fields = ['id', 'name', 'class_name','class_id']

class ClassSerializer(serializers.ModelSerializer):
    streams = StreamSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ['id', 'name', 'streams']

class QuestionSerializer(serializers.ModelSerializer):
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), source='class_name', write_only=True)
    stream_id = serializers.PrimaryKeyRelatedField(queryset=Stream.objects.all(), source='stream_name', write_only=True)
    class_name = serializers.SerializerMethodField()
    stream_name = StreamSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    
    class Meta:
        model = Question
        fields = ['id','text','category', 'category_id','class_id','stream_id','class_name','stream_name']

    def get_class_name(self, obj):
        if obj.class_name:
            return {
             'id': obj.class_name.id,
             'name': obj.class_name.name
        }
        return None


    def validate(self, data):
        class_instance = data.get('class_name')
        stream_instance = data.get('stream_name')

        if stream_instance.class_name != class_instance:
            raise serializers.ValidationError("Selected stream does not belong to the selected class.")

        return data

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
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), source='class_name', write_only=True)
    stream_id = serializers.PrimaryKeyRelatedField(queryset=Stream.objects.all(), source='stream_name', write_only=True)
    class_name = serializers.SerializerMethodField()
    stream_name = StreamSerializer(read_only=True)
    answers = StudentAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = [
            'id', 'name', 'phone', 'gender', 'dob', 'email', 'address',
            'personal_details', 'education_details',
            'class_id', 'stream_id',
            'class_name', 'stream_name',
            'answers'
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
