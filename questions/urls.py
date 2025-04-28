from django.urls import path
from .views import QuestionListCreateAPIView,QuestionRetrieveUpdateDestroyAPIView,ClassListCreateAPIview,ClassRetrieveUpdateDestroyAPIView,StreamListCreateAPIView,StreamRetrieveUpdateDestroyAPIView,CategoryListCreateAPIView,CategoryRetrieveUpdateDestroyAPIView,CareerListCreateAPIView,CareerRetrieveupdateDestroyAPIView

urlpatterns = [
    path("question/",QuestionListCreateAPIView.as_view(),name="question-list-create"),
    path("question/<int:pk>/",QuestionRetrieveUpdateDestroyAPIView.as_view(),name="question-retrieve-update-destroy"),
    path('class/',ClassListCreateAPIview.as_view(),name="class-list-create"),
    path('class/<int:pk>/',ClassRetrieveUpdateDestroyAPIView.as_view(),name="class-retrieve-update-destroy"),
    path('stream/',StreamListCreateAPIView.as_view(),name = "stream-list-create"),
    path("stream/<int:pk>/",StreamRetrieveUpdateDestroyAPIView.as_view(),name="stream-retrieve-update-destroy"),
    path('category/',CategoryListCreateAPIView.as_view(),name="category-list-create"),
    path('category/<int:pk>/',CategoryRetrieveUpdateDestroyAPIView.as_view(),name="category-retrieve-update-destroy"),
    path('careers/', CareerListCreateAPIView.as_view(), name='careers-list-create'),
    path("careers/<int:pk>/",CareerRetrieveupdateDestroyAPIView.as_view(), name="careers-retrieve-update-destroy")

]