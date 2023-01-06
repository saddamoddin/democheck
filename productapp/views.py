from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Student
from .serializer import studentSerializer
# Create your views here.

class studentView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializer