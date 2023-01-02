from django.urls import path
from api import views 
from rest_framework.urlpatterns import format_suffix_patterns
 
urlpatterns = [ 
    path('aiposts/', views.AIPostList.as_view()),
    path('aiposts/<int:pk>/', views.AIPostDetail.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('answers/<int:pk>/', views.AnswerDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)