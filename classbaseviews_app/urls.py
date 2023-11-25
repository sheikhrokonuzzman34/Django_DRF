from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from classbaseviews_app import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    
    # Using mixins
    path('MixinsList/', views.MixinsList.as_view()),
    path('MixinsDetail/<int:pk>/', views.MixinsDetail.as_view()),
    
    
    # Using generic class-based views
    path('GenericList/', views.GenericList.as_view()),
    path('GenericDetail/<int:pk>/', views.GenericDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
