from rest_framework import serializers
from api.models import AIPost, Answer
# AIPost serializer

class AIPostSerializer(serializers.ModelSerializer):
    summary = serializers.CharField(read_only = True) 
    question = serializers.CharField(read_only = True) 

    class Meta:
        model = AIPost
        fields = ['id', 'title', 'text', 'summary', 'question']

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['post', 'correctness', 'answer']


 