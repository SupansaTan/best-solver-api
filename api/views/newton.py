import numpy as np
import matplotlib.pyplot as plt
import timeit
from sympy import Symbol, Derivative


def df(x):
    return -np.exp(-x) - 1

def newton(f,df,x0,epsilon,max_iter):
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


def newton_graph(f,root):
    xmin = float('%.2f' % (root-0.1) )
    xmax = float('%.2f' % (root+0.1) )
    print(xmin , xmax)
    x = np.linspace(xmin , xmax, 1000)
    f1 = f(x)
    plt.plot(x, f1, '-', label=r'$y=e^{-x}$')
    plt.plot(root, f(root), 'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.savefig("newton_py.png")
    return "newton_py.png"


def newton_time(x0,epsilon,max_iter):
    n_time = 10
    SETUP_CODE = '''from __main__ import newton, f, df'''
    TEST_CODE = '''newton(f, df, {}, {}, {})'''.format(x0,epsilon,max_iter)
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = n_time,
                          number = 1
                          )
    print('Used Time : {} ms'.format(sum(times)/n_time*1000))       # repeat 10 times and find average time
    return sum(times)/n_time*1000


# if __name__ == '__main__':
#     eqa = 'np.e**(-x) -x'
#     f = lambda x : eval(eqa)
#     x = Symbol('x')
#     deriv = Derivative(eval(eqa), x)                # function = eval(eqa)
#     df = lambda x0 : deriv.doit().subs(x,x0)

#     x0,epsilon,max_iter = 1.0, 1e-15, 16
#     solution = newton(f, df, x0,epsilon,max_iter)
#     print( 'sol = %.15f' % solution )
#     newton_time( x0,epsilon,max_iter)
#     newton_graph(f,solution)



# ปล
# ใช้ def df(x):
#     return -np.exp(-x) - 1
# Used Time : 0.15329000000003923 ms

# ใช้ x = Symbol('x')
#     # function = eval(eqa)
#     deriv = Derivative(eval(eqa), x)
#     df = lambda x0 : deriv.doit().subs(x,x0)
# Used Time : 2.107440000000027 ms