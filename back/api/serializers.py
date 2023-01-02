from rest_framework import serializers
from api.models import AIPost
# AIPost serializer

class AIPostSerializer(serializers.ModelSerializer):
    summary = serializers.CharField(read_only = True) 
    questions = serializers.CharField(read_only = True) 
    corectness = serializers.CharField(read_only = True) 

    class Meta:
        model = AIPost
        fields = ['id', 'title', 'text', 'summary', 'questions', 'corectness']
 