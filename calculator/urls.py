from django.urls import path
from .views import ConversionCreateAPIView

urlpatterns = [
    path('calculate-percentage/', ConversionCreateAPIView.as_view(), name='calculate-percentage'),
]