from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import StudentData
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        snippets = StudentData.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
  
    
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
 
    try:
        snippet = StudentData.objects.get(pk=pk)
    except StudentData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    