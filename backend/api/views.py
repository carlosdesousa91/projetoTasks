from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, TaskSerializer
from .models import Task

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

