from rest_framework import serializers
from .models import StudentData

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    student_id = serializers.CharField(max_length=20)
    add = serializers.CharField(max_length=500)
    
    def create(self, validated_data):
        return StudentData.objects.create(**validated_data)