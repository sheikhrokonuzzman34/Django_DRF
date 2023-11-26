from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from classbaseviews_app import views
from .views import *



urlpatterns = [
    # Using mixins
    path('MixinsList/', views.MixinsList.as_view()),
    path('MixinsDetail/<int:pk>/', views.MixinsDetail.as_view()),
    
    
    # Using generic class-based views
    path('GenericList/', views.GenericList.as_view()),
    path('GenericDetail/<int:pk>/', views.GenericDetail.as_view()),
    
    
    
    path('api/', views.api_root),
    path('snippets/',views.SnippetList.as_view(),name='snippet-list'),
    path('snippets/<int:pk>/',views.SnippetDetail.as_view(),name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
