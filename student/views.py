from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer

# Create your views here.

class StudentOperation(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer