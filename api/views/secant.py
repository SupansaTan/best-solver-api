# https://personal.math.ubc.ca/~pwalls/math-python/roots-optimization/secant/
from rest_framework import generics
from api.serializers import ResultSerializer
import urllib, json, coreapi, coreschema
from urllib.error import HTTPError
from rest_framework.response import Response
import numpy as np
import matplotlib.pyplot as plt
import time

class Secant(generics.ListAPIView):
    serializer_class = ResultSerializer
    a,b = 0.4,0.6

    def get(self, request):
        body = {}
        sol = self.secant(self.f,self.a,self.b)
        body['result'] = sol
        body['time'] = self.secant_time()
        body['graph'] = self.secant_graph(self.f,self.a,self.b,sol)
        return Response(body)

    def f(self,x):
        return np.exp(-x) -x

    def secant(self,f,a,b,N=20):
        if f(a)*f(b) >= 0:
            print("Secant method fails.")
            return None
        a_n = a
        b_n = b
        for n in range(1,N+1):
            m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
            f_m_n = f(m_n)
            if f(a_n)*f_m_n < 0:
                a_n = a_n
                b_n = m_n
            elif f(b_n)*f_m_n < 0:
                a_n = m_n
                b_n = b_n
            elif f_m_n == 0:
                print("Found exact solution.")
                return m_n
            else:
                print("Secant method fails.")
                return None
        return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

    def secant_graph(self,f,a,b,root):
        x = np.linspace(a,b, 1000)
        f1 = f(x)
        plt.plot(x, f1, '-')
        plt.plot(root, f(root), 'ro')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid()
        plt.savefig("secant_py.png")
        return "secant_py.png"

    def secant_time(self):
        t1 = time.time()
        n_time = 100
        for i in range(n_time):
            self.secant(self.f,self.a,self.b)
        t2 = time.time()
        return (t2*1000-t1*1000)/n_time