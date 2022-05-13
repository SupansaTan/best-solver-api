from rest_framework import generics
from api.serializers import ResultSerializer
import urllib, json, coreapi, coreschema
from urllib.error import HTTPError
from rest_framework.response import Response
import numpy as np
import matplotlib.pyplot as plt
import time

class Trapezoid(generics.ListAPIView):
    serializer_class = ResultSerializer
    a = 0; b = 5;N = 20

    def get(self, request):
        body = {}
        sol = self.trapz(self.f,self.a,self.b,self.N)
        body['result'] = sol
        body['time'] = self.trapz_time()
        body['graph'] = self.trapz_graph(self.f,self.a,self.b,self.N)
        return Response(body)

    def f(self,x):
        return 1/(1 + x**2)

    def trapz(self,f,a,b,N):
        x = np.linspace(a,b,N+1)
        y = f(x)
        y_right = y[1:] # Right endpoints
        y_left = y[:-1] # Left endpoints
        dx = (b - a)/N
        T = (dx/2) * np.sum(y_right + y_left)
        return T

    def trapz_graph(self,f,a,b,N):
        x = np.linspace(a,b, N+1)
        for i in range(N):
            xs = [x[i],x[i],x[i+1],x[i+1]]
            ys = [0,f(x[i]),f(x[i+1]),0]
            plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)
        plt.title('Trapezoid Rule, N = {}'.format(N))
        plt.legend()
        plt.grid()
        plt.savefig("trapezoid_py.png")
        return "trapezoid_py.png"

    def trapz_time(self):
        t1 = time.time()
        n_time = 100
        for _ in range(n_time):
            self.trapz(self.f,self.a,self.b,self.N)
        t2 = time.time()
        return (t2*1000-t1*1000)/n_time