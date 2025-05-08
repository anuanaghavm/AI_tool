from rest_framework import generics, status
from rest_framework.response import Response
from .models import Subject, Percentage
from .serializers import SubjectSerializer, PercentageSerializer

class SubjectCreateView(generics.CreateAPIView):
    serializer_class = SubjectSerializer

    def post(self, request):
        subjects = request.data.get('subjects', [])

        if not subjects:
            return Response({"error": "Subjects are required"}, status=400)

        # Save each subject
        for subject in subjects:
            serializer = SubjectSerializer(data=subject)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)

        return Response({"message": "Subjects and grades added successfully"}, status=status.HTTP_201_CREATED)

class CalculatePercentageView(generics.GenericAPIView):
    serializer_class = PercentageSerializer

    def get(self, request):
        subjects = Subject.objects.all()
        if not subjects.exists():
            return Response({'error': 'No subjects found'}, status=status.HTTP_400_BAD_REQUEST)

        total_obtained_marks = sum(sub.obtained_marks for sub in subjects if sub.obtained_marks is not None)
        total_possible_marks = sum(sub.total_marks for sub in subjects if sub.total_marks is not None)

        if total_possible_marks > 0:
            percentage = (total_obtained_marks / total_possible_marks) * 100
        else:
            total_marks = sum(sub.marks for sub in subjects if sub.marks is not None)
            total_subjects = subjects.count()
            percentage = total_marks / total_subjects if total_subjects > 0 else 0

        percentage_obj, _ = Percentage.objects.update_or_create(
            defaults={'percentage': percentage}
        )

        serializer = self.get_serializer(percentage_obj)
        return Response(serializer.data)