from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import generics
from rest_framework import generics, permissions

# Create your views here.
class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Only an authenticated user can access this API endpoint
    permission_classes = [permissions.IsAuthenticated]

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Only an authenticated user can access this API endpoint
    permission_classes = [permissions.IsAuthenticated]