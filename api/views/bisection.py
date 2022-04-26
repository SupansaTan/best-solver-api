import numpy as np
import matplotlib.pyplot as plt
import timeit

def bisection(f,a,b,tol):
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
    # print('a = {}  , b = {}'.format(a,b))
    return m

def bisection_graph(f,a,b,m):
    x = np.linspace(a,b, 1000)
    y = np.exp(-x) -x
    plt.plot(x, y, '-', label=r'$y=e^{-x}$')
    plt.plot(m, f(m), 'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.savefig("bisection_py.png")
    return "bisection_py.png"

def bisection_time(a,b,tol):
    n_time = 10
    SETUP_CODE = '''from __main__ import bisection, f'''
    TEST_CODE = '''bisection(f,{},{},{})'''.format(a,b,tol)
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = n_time,
                          number = 1
                          )
    print('Used Time : {} ms'.format(sum(times)/n_time*1000))       # repeat 10 times and find average time   
    return sum(times)/n_time*1000

# if __name__ == '__main__':
#     eqa = 'np.exp(-x) -x'
#     f = lambda x : eval(eqa)

#     tol, a, b = 0.001, 0.4, 0.6
#     sol = bisection(f,a,b,tol)
#     print('sol = ',sol)
#     bisection_time(a,b,tol)
#     bisection_graph(f,a,b,sol)