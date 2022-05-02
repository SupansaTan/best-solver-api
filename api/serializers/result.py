from rest_framework import serializers

class ResultSerializer(serializers.Serializer):
  result = serializers.FloatField()
  time_used = serializers.FloatField()
  graph = serializers.CharField()