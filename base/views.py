from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Job, JobApplication, Message, Category
from .serializers import JobSerializer, JobApplicationSerializer, MessageSerializer, CategorySerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobApplicationViewSet(ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

