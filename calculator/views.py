from rest_framework import generics, status
from rest_framework.response import Response
from .models import  Subject, Percentage
from .serializers import  SubjectBulkCreateSerializer, PercentageSerializer
from students.serializers import StudentSerializer
from students.models import Student


# students/views.py

class SubjectCreateView(generics.CreateAPIView):
    serializer_class = SubjectBulkCreateSerializer  # Ensure you use the correct serializer

    def post(self, request):
        student_uuid = request.data.get('student_uuid')
        subjects = request.POST.getlist('subject')
        grades = request.POST.getlist('grade')

        if len(subjects) != len(grades):
            return Response({"error": "Subjects and grades count mismatch"}, status=400)

        # Fetch the student instance based on the UUID
        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)

        # Now, create the Subject instances
        for subject, grade in zip(subjects, grades):
            Subject.objects.create(
                student=student,  # Use the student instance, not the UUID directly
                name=subject,     # Set the subject name
                grade=grade       # Set the grade
            )

        return Response({"message": "Subjects and grades added successfully"}, status=status.HTTP_201_CREATED)



class CalculatePercentageView(generics.GenericAPIView):
    serializer_class = PercentageSerializer

    def post(self, request):
        student_uuid = request.data.get('student_uuid')
        try:
            student = Student.objects.get(student_uuid=student_uuid)  # ✅ Fixed
        except Student.DoesNotExist:
            return Response({'error': 'Invalid student UUID'}, status=status.HTTP_404_NOT_FOUND)

        subjects = Subject.objects.filter(student=student)
        if not subjects.exists():
            return Response({'error': 'No subjects found for student'}, status=status.HTTP_400_BAD_REQUEST)

        total_marks = sum(sub.marks for sub in subjects if sub.marks is not None)
        total_subjects = subjects.count()
        percentage = total_marks / total_subjects

        percentage_obj, _ = Percentage.objects.update_or_create(
            student=student,
            defaults={'percentage': percentage}
        )
        serializer = self.get_serializer(percentage_obj)
        return Response(serializer.data)
    

    def get(self, request):
        student_uuid = request.query_params.get('student_uuid')
        if not student_uuid:
            return Response({'error': 'student_uuid is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExist:
            return Response({'error': 'Invalid student UUID'}, status=status.HTTP_404_NOT_FOUND)

        subjects = Subject.objects.filter(student=student)
        if not subjects.exists():
            return Response({'error': 'No subjects found for student'}, status=status.HTTP_400_BAD_REQUEST)

        total_marks = sum(sub.marks for sub in subjects if sub.marks is not None)
        total_subjects = subjects.count()
        percentage = total_marks / total_subjects

        percentage_obj, _ = Percentage.objects.update_or_create(
            student=student,
            defaults={'percentage': percentage}
        )

        serializer = self.get_serializer(percentage_obj)
        return Response(serializer.data)
