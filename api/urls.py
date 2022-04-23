from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Best Solver API')

urlpatterns = [
  path('', schema_view, name='swagger-ui'),  # still error because don't have any api
]