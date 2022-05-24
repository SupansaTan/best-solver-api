from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from api import views

app_name = 'api'
schema_view = get_swagger_view(title='Best Solver API')

urlpatterns = [
  path('', schema_view, name='swagger-ui'),  # still error because don't have any api
  path('root', views.Root.as_view(), name='root-finding'),
  path('bisection/<int:id>', views.Bisection.as_view(), name='root-bisection'),
  path('falsi/<int:id>', views.Falsi.as_view(), name='root-falsi'),
  path('newton/<int:id>', views.Newton.as_view(), name='root-newton'),
  path('secant/<int:id>', views.Secant.as_view(), name='root-secant'),
  path('reimann/<int:id>', views.Reimann.as_view(), name='integral-reimann'),
  path('trapezoid/<int:id>', views.Trapezoid.as_view(), name='integral-trapezoid'),
  path('simpson/<int:id>', views.Simpson.as_view(), name='integral-simpson'),
]