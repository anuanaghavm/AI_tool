from django.shortcuts import render
from .models import Student,StudentAnswer,Personal,Education
from .serializers import StudentAnswerSerializer,StudentSerializer,PersonalSerializer,EducationSerializer
from rest_framework import generics,status
from rest_framework.response import Response

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the student in the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


