from django.urls import path
from .views import SubjectCreateView, CalculatePercentageView

urlpatterns = [
    path('subjects/create/', SubjectCreateView.as_view(), name='subject-create'),
    path('calculate-percentage/', CalculatePercentageView.as_view(), name='calculate-percentage'),
]