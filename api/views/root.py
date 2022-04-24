from rest_framework import generics
from api.serializers import ResultSerializer
import urllib, json, coreapi, coreschema
from urllib.error import HTTPError
from rest_framework.response import Response

class Root(generics.ListAPIView):
  serializer_class = ResultSerializer

  def get(self, request):
    return Response({ 'test': 0.00 })


