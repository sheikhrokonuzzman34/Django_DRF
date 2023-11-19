
from django.contrib import admin
from django.urls import path

from new_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('hh/<int:pk>/', student_details ,name='student_details'),
    path('student_data_create/', student_data_create ,name='student_data_create'),
=======
    path('hh', student_details ,name='student_details'),
>>>>>>> 3e25e3e2d05eff581fdfa35ac46d5e57c4b2acae
]
