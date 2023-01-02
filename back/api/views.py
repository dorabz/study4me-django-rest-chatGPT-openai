from rest_framework import views, generics, permissions
from api.models import AIPost, Answer
from api import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render


class AIPostList(generics.ListCreateAPIView):
    queryset = AIPost.objects.all()
    serializer_class = serializers.AIPostSerializer
    #permission_classes = [permissions.AllowAny]


class AIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AIPost.objects.all()
    serializer_class = serializers.AIPostSerializer
    #permission_classes = [permissions.AllowAny]


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    #permission_classes = [permissions.AllowAny]

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    #permission_classes = [permissions.AllowAny]





