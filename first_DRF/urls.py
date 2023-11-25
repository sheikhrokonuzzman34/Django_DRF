from django.contrib import admin
from django.urls import path

from new_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/', student_list, name='student_list'),
    path('student_detail/<int:pk>/', student_detail, name='student_detail'),  
]
