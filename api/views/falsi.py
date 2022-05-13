# https://www.codesansar.com/numerical-methods/false-position-method-python-program.htm
from rest_framework import generics
from api.serializers import ResultSerializer
import urllib, json, coreapi, coreschema
from urllib.error import HTTPError
from rest_framework.response import Response
import numpy as np
import matplotlib.pyplot as plt
import time

class Falsi(generics.ListAPIView):
    serializer_class = ResultSerializer
    tol, a, b = 0.001, 0.4, 0.6

    def get(self, request):
        body = {}
        sol = self.falsi(self.f,self.a,self.b,self.tol)
        body['result'] = sol
        body['time_used'] = self.falsi_time()
        body['graph'] = self.falsi_graph(self.f,self.a,self.b,sol)
        return Response(body)
    
    def f(self,x):
        return np.exp(-x) -x

    def falsi(self,f,a,b,tol=0.001):
        step = 1
        if f(a) * f(b) >= 0.0:
            print('Try Again with different guess values.')
            return None
        else:
            condition = True
            while condition:
                x2 = a - (b-a) * f(a)/( f(b) - f(a) )

                if f(a) * f(x2) < 0:
                    b = x2
                else:
                    a = x2

                step = step + 1
                condition = abs(f(x2)) > tol
        return x2

    def falsi_graph(self,f,a,b,root):
        x = np.linspace(a,b, 1000)
        f1 = f(x)
        plt.plot(x, f1, '-')
        plt.plot(root, f(root), 'ro')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid()
        plt.savefig("falsi_py.png")
        plt.close()
        return "falsi_py.png"

    def falsi_time(self):
        t1 = time.time()
        n_time = 100
        for i in range(n_time):
            self.falsi(self.f,self.a,self.b,self.tol)
        t2 = time.time()
        return (t2*1000-t1*1000)/n_time