from django.urls import path
from .views import QuestionListCreateAPIView,QuestionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("question/",QuestionListCreateAPIView.as_view(),name="question-list-create"),
    path("question/<int:pk>/",QuestionRetrieveUpdateDestroyAPIView.as_view(),name="question-retrieve-update-destroy"),
]