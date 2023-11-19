from django.shortcuts import render
from .models import StudentData
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

<<<<<<< HEAD
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.r

@csrf_exempt
def student_data_create(request):
    if request.method == 'POST':
        json_data = request.body
        # Check if JSON data is empty
        if not json_data:
            error_response = {'error': 'Empty JSON data'}
            json_data = JSONRenderer().render(error_response)
            return HttpResponse(json_data, content_type='application/json')

        stremn = io.BytesIO(json_data)
        python_data = JSONParser().parse(stremn)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response_data = {'success': 'Successfully created'}
            json_data = JSONRenderer().render(response_data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
        
        
def student_details(request ,pk):
    sut = StudentData.objects.get(id = pk)
    serializer = StudentSerializer(sut)
    jason_data = JSONRenderer().render(serializer.data)
    return HttpResponse(jason_data,content_type='application/json')        
            
        
        
    
=======
# Create your views here.r

def student_details(request):
    sut = StudentData.objects.get(id = 2)
    print(sut)
    serializer = StudentSerializer(sut)
    jason_data = JSONRenderer().render(serializer.data)
    return HttpResponse(jason_data,content_type='application/json')
>>>>>>> 3e25e3e2d05eff581fdfa35ac46d5e57c4b2acae
