from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    student_id = serializers.CharField(max_length=20)
    add = serializers.CharField(max_length=500)