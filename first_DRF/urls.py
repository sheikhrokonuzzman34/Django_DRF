
from django.contrib import admin
from django.urls import path

from new_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hh/<int:pk>/', student_details ,name='student_details'),
    path('student_data_create/', student_data_create ,name='student_data_create'),
]
