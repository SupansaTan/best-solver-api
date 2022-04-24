from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from api import views

app_name = 'api'
schema_view = get_swagger_view(title='Best Solver API')

urlpatterns = [
  path('', schema_view, name='swagger-ui'),  # still error because don't have any api
  path('root', views.Root.as_view(), name='find-root'),
]