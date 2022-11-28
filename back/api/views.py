from rest_framework import views, generics, permissions
from api.models import AIPost
from api import serializers


class AIPostList(generics.ListCreateAPIView):
    queryset = AIPost.objects.all()
    serializer_class = serializers.AIPostSerializer
    #permission_classes = [permissions.AllowAny]


class AIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AIPost.objects.all()
    serializer_class = serializers.AIPostSerializer
    #permission_classes = [permissions.AllowAny]