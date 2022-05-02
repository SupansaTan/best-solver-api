from rest_framework import generics
from sympy import N
from api.serializers import ResultSerializer
import urllib, json, coreapi, coreschema
from urllib.error import HTTPError
from rest_framework.response import Response
import numpy as np
import matplotlib.pyplot as plt
import time

class Bisection(generics.ListAPIView):
    serializer_class = ResultSerializer
    tol, a, b = 0.001, 0.4, 0.6

    def get(self, request):
        body = {}
        sol = self.bisection(self.f,self.a,self.b,self.tol)
        body['result'] = sol
        body['time'] = self.bisection_time()
        body['graph'] = self.bisection_graph(self.f,self.a,self.b,sol)
        return Response(body)

    def f(self,x):
        return np.exp(-x) -x

    def bisection(self,f,a,b,tol):
        fa,fb = f(a), f(b)
        n = 1 
        while (b-a) > tol:
            m = a + (b-a)/2.0
            fm = f(m)
            n += 1
            if np.sign(fa) == np.sign(fm):
                a, fa = m, fm
            else:
                b, fb = m, fm
        return m

    def bisection_graph(self,f,a,b,m):
        x = np.linspace(a,b, 1000)
        y = np.exp(-x) -x
        plt.plot(x, y, '-')
        plt.plot(m, f(m), 'ro')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid()
        plt.savefig("bisection_py.png")
        return "bisection_py.png"

    def bisection_time(self):
        t1 = time.time()
        n_time = 100
        for i in range(n_time):
            self.bisection(self.f,self.a,self.b,self.tol)
        t2 = time.time()
        return (t2*1000-t1*1000)/n_time
        
