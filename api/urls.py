from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from api import views

app_name = 'api'
schema_view = get_swagger_view(title='Best Solver API')

urlpatterns = [
  path('', schema_view, name='swagger-ui'),  # still error because don't have any api
  path('Bisection/<int:id>', views.Bisection.as_view(), name='root-bisection'),
  path('RegulaFalsi/<int:id>', views.Falsi.as_view(), name='root-falsi'),
  path('Newton/<int:id>', views.Newton.as_view(), name='root-newton'),
  path('Secant/<int:id>', views.Secant.as_view(), name='root-secant'),
  path('RiemannSum/<int:id>', views.Reimann.as_view(), name='integral-reimann'),
  path('TrapezoidRule/<int:id>', views.Trapezoid.as_view(), name='integral-trapezoid'),
  path('SimsonRule/<int:id>', views.Simpson.as_view(), name='integral-simpson'),
]