from django.contrib import admin
from django.urls import path,include

from new_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('student_list/', student_list, name='student_list'),
    path('student_detail/<int:pk>/', student_detail, name='student_detail'),  
=======
    path('api/', include('product_app.urls')),
    path('student_data_create/', student_data_create, name='student_data_create'),
    path('hh/', student_details, name='student_details'),  # No integer parameter
    path('hh/<int:pk>/', student_details, name='student_details_with_pk'),  # With integer parameter
>>>>>>> dd82612e43b433ece3b290507fd59c599b4c9134
]
