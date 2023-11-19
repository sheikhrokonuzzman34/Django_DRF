from rest_framework import serializers
<<<<<<< HEAD
from .models import StudentData
=======
>>>>>>> 3e25e3e2d05eff581fdfa35ac46d5e57c4b2acae

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    student_id = serializers.CharField(max_length=20)
<<<<<<< HEAD
    add = serializers.CharField(max_length=500)
    
    def create(self, validated_data):
        return StudentData.objects.create(**validated_data)
=======
    add = serializers.CharField(max_length=500)
>>>>>>> 3e25e3e2d05eff581fdfa35ac46d5e57c4b2acae
