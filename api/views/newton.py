from rest_framework import generics
from api.serializers import ResultSerializer
import urllib, json, coreapi, coreschema
from urllib.error import HTTPError
from rest_framework.response import Response
import numpy as np
import matplotlib.pyplot as plt
import time
from api.constant.function import getFunction, getDiffFunction
import api.constant.variable as var
import base64

class Newton(generics.ListAPIView):
    serializer_class = ResultSerializer
    x0,epsilon,max_iter = var.x0, var.epsilon, var.max_iter
    id = 1

    def get(self, request, id):
        self.id = id
        body = {}
        sol = self.newton(self.f, self.df, self.x0,self.epsilon,self.max_iter)
        body['result'] = sol
        body['time'] = self.newton_time()
        body['graph'] = self.newton_graph(self.f,sol)
        return Response(body)
    
    def f(self,x):
        func = getFunction(self.id)
        return func(x)

    def df(self,x):
        dfunc = getDiffFunction(self.id)
        return dfunc(x)

    def newton(self,f,df,x0,epsilon,max_iter):
        xn = x0
        for n in range(0,max_iter):
            fxn = f(xn)
            if abs(fxn) < epsilon:
                # print('Found solution after',n,'iterations.')
                return xn
            dfxn = df(xn)
            if dfxn == 0:
                print('Zero derivative. No solution found.')
                return None
            xn = xn - fxn/dfxn
        print('Exceeded maximum iterations. No solution found.')
        return None


    def newton_graph(self,f,root):
        xmin = float('%.2f' % (root-0.1) )
        xmax = float('%.2f' % (root+0.1) )
        x = np.linspace(xmin , xmax, 1000)
        f1 = f(x)
        plt.plot(x, f1, '-')
        plt.plot(root, f(root), 'ro')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid()
        plt.savefig("newton_py.png")
        plt.close()
        with open("newton_py.png", "rb") as f:
            png_encoded = base64.b64encode(f.read())
        return png_encoded


    def newton_time(self):
        t1 = time.time()
        n_time = 100
        for i in range(n_time):
            self.newton(self.f, self.df, self.x0,self.epsilon,self.max_iter)
        t2 = time.time()
        return (t2*1000-t1*1000)/n_time

