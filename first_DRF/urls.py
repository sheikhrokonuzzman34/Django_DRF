from django.contrib import admin
from django.urls import path,include

from new_app.views import student_details, student_data_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product_app.urls')),
    path('student_data_create/', student_data_create, name='student_data_create'),
    path('hh/', student_details, name='student_details'),  # No integer parameter
    path('hh/<int:pk>/', student_details, name='student_details_with_pk'),  # With integer parameter
]
