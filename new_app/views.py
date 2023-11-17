from django.shortcuts import render
from .models import StudentData
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.r

def student_details(request):
    sut = StudentData.objects.get(id = 2)
    print(sut)
    serializer = StudentSerializer(sut)
    jason_data = JSONRenderer().render(serializer.data)
    return HttpResponse(jason_data,content_type='application/json')