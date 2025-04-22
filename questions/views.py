from django.shortcuts import render
from .models import Question,Student,StudentAnswer,Personal,Education,Class,Stream,Category
from .serializers import QuestionSerializer,StudentAnswerSerializer,StudentSerializer,PersonalSerializer,EducationSerializer,ClassSerializer,StreamSerializer,CategorySerializer
from rest_framework import generics,status

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentAnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer

class StudentAnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentAnswer.objects.all()
    serializer_class =StudentAnswerSerializer

class PersonalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class PersonalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class EducationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ClassListCreateAPIview(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class StreamListCreateAPIView(generics.ListCreateAPIView):
    queryset= Stream.objects.all()
    serializer_class = StreamSerializer

class StreamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer