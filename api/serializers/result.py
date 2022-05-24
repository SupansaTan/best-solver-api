from rest_framework import serializers

class ResultSerializer(serializers.Serializer):
  result = serializers.CharField()
  time_used = serializers.CharField()
  graph = serializers.CharField()