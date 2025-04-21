from django.urls import path
from .views import QuestionListCreateAPIView,QuestionRetrieveUpdateDestroyAPIView,StudentListCreateAPIView,StudentRetrieveUpdateDestroyAPIView,StudentAnswerListCreateAPIView,StudentAnswerRetrieveUpdateDestroyAPIView,PersonalListCreateAPIView,PersonalRetrieveUpdateDestroyAPIView,EducationListCreateAPIView,EducationRetrieveUpdateDestroyAPIView,ClassListCreateAPIview,ClassRetrieveUpdateDestroyAPIView,StreamListCreateAPIView,StreamRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("question/",QuestionListCreateAPIView.as_view(),name="question-list-create"),
    path("question/<int:pk>/",QuestionRetrieveUpdateDestroyAPIView.as_view(),name="question-retrieve-update-destroy"),
    path('student/',StudentListCreateAPIView.as_view(),name="student-list-create"),
    path('student/<int:pk>/',StudentRetrieveUpdateDestroyAPIView.as_view(),name="student-retrieve-update-destroy"),
    path('student-answer/',StudentAnswerListCreateAPIView.as_view(),name="studentanswer-list-create"),
    path("student-answer/<int:pk>/",StudentAnswerRetrieveUpdateDestroyAPIView.as_view(),name="studentanswer-retrieve-update-destroy"),
    path("personal/",PersonalListCreateAPIView.as_view(), name="personal-list-create"),
    path("personal/<int:pk>/",PersonalRetrieveUpdateDestroyAPIView.as_view(),name="personal-retrieve-update-destroy"),
    path('education/',EducationListCreateAPIView.as_view(),name="education-list-create"),
    path('education/<int:pk>/',EducationRetrieveUpdateDestroyAPIView.as_view(),name="education-retrieve-update-destroy"),
    path('class/',ClassListCreateAPIview.as_view(),name="class-list-create"),
    path('class/<int:pk>/',ClassRetrieveUpdateDestroyAPIView.as_view(),name="class-retrieve-update-destroy"),
    path('stream/',StreamListCreateAPIView.as_view(),name = "stream-list-create"),
    path("stream/<int:pk>/",StreamRetrieveUpdateDestroyAPIView.as_view(),name="stream-retrieve-update-destroy")
]