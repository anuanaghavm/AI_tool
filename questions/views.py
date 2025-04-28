from django.shortcuts import render
from .models import Question,Class,Stream,Category,Career
from .serializers import QuestionSerializer,ClassSerializer,StreamSerializer,CategorySerializer,CareerSerializer
from rest_framework import generics,status
from rest_framework.response import Response

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CareerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class CareerRetrieveupdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer 

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

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