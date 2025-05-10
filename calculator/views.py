from rest_framework import generics, status
from rest_framework.response import Response
from .models import Conversion
from .serializers import  ConversionSerializer

class ConversionCreateAPIView(generics.CreateAPIView):
    queryset = Conversion.objects.all()
    serializer_class = ConversionSerializer