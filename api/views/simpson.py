from rest_framework import generics
from api.serializers import ResultSerializer
import urllib, json, coreapi, coreschema
from urllib.error import HTTPError
from rest_framework.response import Response
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import time
from api.constant.function import getFunction
import api.constant.variable as var
import base64

class Simpson(generics.ListAPIView):
    serializer_class = ResultSerializer
    a = 0; b = 5;N = 20
    id = 1

    def get(self, request, id):
        self.id = id
        body = {}
        sol = self.simps(self.f,self.a,self.b,self.N)
        body['result'] = '{:.15f}'.format(sol)
        body['time'] = '{:.3f}'.format(self.simps_time())
        body['graph'] = self.simps_graph(self.f,self.a,self.b,self.N)
        return Response(body)

    def f(self,x):
        func = getFunction(self.id)
        return func(x)
        
    def simps(self,f,a,b,N):
        if N % 2 == 1:
            raise ValueError("N must be an even integer.")
        dx = (b-a)/N
        x = np.linspace(a,b,N+1)
        y = f(x)
        sum = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
        return sum

    def simps_graph(self,f,a,b,N):
        integrals = []
        x_range = []
        y_range = []
        x = np.linspace(a,b,N)
        for i in x:
            x_range.append(i)
            y_range.append(f(i))
            integral = integrate.simps(y_range, x_range)
            integrals.append(integral)
        plt.plot(x, integrals)
        plt.title("Simpson's Rule, N = {}".format(N))
        plt.legend()
        plt.grid()
        plt.savefig("simpson_py.png")
        plt.close()
        with open("simpson_py.png", "rb") as f:
            png_encoded = base64.b64encode(f.read())
        return png_encoded

    def simps_time(self):
        t1 = time.time()
        n_time = 100
        for _ in range(n_time):
            self.simps(self.f,self.a,self.b,self.N)
        t2 = time.time()
        return (t2*1000-t1*1000)/n_time