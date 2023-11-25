from django.contrib import admin
from django.urls import path,include

from new_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('classbaseviews_app.urls')),
    path('student_list/', student_list, name='student_list'),
    path('student_detail/<int:pk>/', student_detail, name='student_detail'),  

]
