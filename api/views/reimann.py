from rest_framework import generics
from api.serializers import ResultSerializer
import urllib, json, coreapi, coreschema
from urllib.error import HTTPError
from rest_framework.response import Response
import numpy as np
import matplotlib.pyplot as plt
import time
from api.constant.function import getFunction
import api.constant.variable as var

class Reimann(generics.ListAPIView):
    serializer_class = ResultSerializer
    a = var.a; b = var.b; N = var.N
    id = 1

    def get(self, request, id):
        self.id = id
        body = {}
        sol = self.MidPoint_Riemann(self.f,self.a,self.b,self.N)
        body['result'] = sol
        body['time'] = self.reimann_time()
        body['graph'] = self.reimann_graph(self.f,self.a,self.b,self.N)
        return Response(body)

    def f(self,x):
        func = getFunction(self.id)
        return func(x)

    def MidPoint_Riemann(self,f,a,b,N):
        dx = (b-a)/N # subinterval width
        x = np.linspace(a,b,N+1) # array of subintervals
        x_mid = (x[:-1] + x[1:])/2 # array of mid points
        return np.sum( f(x_mid)*dx )

    def reimann_graph(self,f,a,b,N):
        x = np.linspace(a,b, N+1)
        x_mid = (x[:-1] + x[1:])/2 # Midpoints
        y_mid = f(x_mid)
        plt.plot(x_mid,y_mid,'b.',markersize=10)
        plt.bar(x_mid,y_mid,width=(b-a)/N, alpha=0.2, edgecolor='b')
        plt.title('Midpoint Riemann Sum, N = {}'.format(N))
        plt.legend()
        plt.grid()
        plt.savefig("reimann_py.png")
        plt.close()
        return "reimann_py.png"

    def reimann_time(self):
        t1 = time.time()
        n_time = 100
        for _ in range(n_time):
            self.MidPoint_Riemann(self.f,self.a,self.b,self.N)
        t2 = time.time()
        return (t2*1000-t1*1000)/n_time