from django.urls import path
from .views import StudentListCreateAPIView,StudentRetrieveUpdateDestroyAPIView,StudentAnswerListCreateAPIView,StudentAnswerRetrieveUpdateDestroyAPIView,PersonalListCreateAPIView,PersonalRetrieveUpdateDestroyAPIView,EducationListCreateAPIView,EducationRetrieveUpdateDestroyAPIView,StudentAssessmentListCreateAPIView,StudentAssessmentretrieveUpdateDestroyAPIView,ResultCreateView,ResultListView


urlpatterns = [

    path('student/',StudentListCreateAPIView.as_view(),name="student-list-create"),
    path('student/<uuid:student_uuid>/',StudentRetrieveUpdateDestroyAPIView.as_view(),name="student-retrieve-update-destroy"),
    path('student-answer/',StudentAnswerListCreateAPIView.as_view(),name="studentanswer-list-create"),
    path("student-answer/<int:pk>/",StudentAnswerRetrieveUpdateDestroyAPIView.as_view(),name="studentanswer-retrieve-update-destroy"),
    path("personal/",PersonalListCreateAPIView.as_view(), name="personal-list-create"),
    path("personal/<int:pk>/",PersonalRetrieveUpdateDestroyAPIView.as_view(),name="personal-retrieve-update-destroy"),
    path('education/',EducationListCreateAPIView.as_view(),name="education-list-create"),
    path('education/<int:pk>/',EducationRetrieveUpdateDestroyAPIView.as_view(),name="education-retrieve-update-destroy"),
    path('student-confirm/',StudentAssessmentListCreateAPIView.as_view(),name="student-list-create"),
    path('student-confirm/<int:pk>/',StudentAssessmentretrieveUpdateDestroyAPIView.as_view(),name="student-retrieve-update-destroy"),
    path('result-create/',ResultCreateView.as_view(),name="result-list-create"),
    path('result/<uuid:student_uuid>/', ResultListView.as_view(), name='result-list'),

]