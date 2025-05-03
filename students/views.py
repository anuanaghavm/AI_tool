from django.shortcuts import render
from .models import Student,StudentAnswer,Personal,Education,StudentAssessment,Result
from .serializers import StudentAnswerSerializer,StudentSerializer,PersonalSerializer,EducationSerializer,StudentAssessmentSerializer,ResultSerializer
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
    lookup_field ="student_uuid"

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

class StudentAssessmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentAssessment.objects.all()
    serializer_class = StudentAssessmentSerializer

class StudentAssessmentretrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentAssessment.objects.all()
    serializer_class = StudentAnswerSerializer

class ResultCreateView(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class ResultListView(generics.ListAPIView):
    serializer_class = ResultSerializer

    def get_queryset(self):
        student_uuid = self.kwargs.get('student_uuid')
        return Result.objects.filter(student__student_uuid=student_uuid)