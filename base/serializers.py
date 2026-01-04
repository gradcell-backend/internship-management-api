from rest_framework import serializers
from .models import Job, JobApplication, Message, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
