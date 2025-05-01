from rest_framework import serializers
from .models import Question,Class,Stream,Category,Career


class CareerSerializer(serializers.ModelSerializer):
    education_pathway = serializers.ListField(
        child=serializers.CharField(), allow_null=True, required=False
    )
    class Meta:
        model = Career
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    careers = CareerSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'careers']


class StreamSerializer(serializers.ModelSerializer):
    class_name = serializers.StringRelatedField(read_only=True)
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), source='class_name', write_only=True)

    class Meta:
        model = Stream
        fields = ['id', 'name', 'class_name', 'class_id']


    class Meta:
        model = Stream
        fields = ['id', 'name', 'class_name', 'class_id']
        read_only_fields = ['id']  # Make ID read-only to prevent None values

class ClassSerializer(serializers.ModelSerializer):
    streams = StreamSerializer(many=True, read_only=True)
    class Meta:
        model = Class
        fields = ['id', 'name', 'streams']

class QuestionSerializer(serializers.ModelSerializer):
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), source='class_name', write_only=True)
    stream_id = serializers.PrimaryKeyRelatedField(queryset=Stream.objects.all(), source='stream_name', write_only=True)
    class_name = serializers.StringRelatedField(read_only=True)
    stream_name = serializers.StringRelatedField(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True, required=False)
    category = CategorySerializer(read_only=True)  # Use the CategorySerializer

    class Meta:
        model = Question
        fields = ['id', 'text', 'class_id', 'stream_id', 'class_name', 'stream_name', 'category_id', 'category','dimension', 'Primary_trait', 'Secondary_trait']


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

