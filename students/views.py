from django.shortcuts import render
from .models import Student,StudentAnswer,Personal,Education,StudentAssessment,Result
from .serializers import StudentAnswerSerializer,StudentSerializer,PersonalSerializer,EducationSerializer,StudentAssessmentSerializer,ResultSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Inline Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Customize the page size here
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the student in the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Student Retrieve, Update, Destroy API (No Pagination)
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "student_uuid"


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