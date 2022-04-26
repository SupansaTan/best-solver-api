# https://www.codesansar.com/numerical-methods/false-position-method-python-program.htm

import numpy as np
import matplotlib.pyplot as plt
import timeit


def falsi(f,a,b,tol=0.001):
    step = 1
    if f(a) * f(b) >= 0.0:
        print('Try Again with different guess values.')
        return None
    else:
        condition = True
        while condition:
            x2 = a - (b-a) * f(a)/( f(b) - f(a) )
            # print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

            if f(a) * f(x2) < 0:
                b = x2
            else:
                a = x2

            step = step + 1
            condition = abs(f(x2)) > tol

    return x2

def falsi_plot(f,a,b,root):
    x = np.linspace(a,b, 1000)
    f1 = f(x)
    plt.plot(x, f1, '-', label=r'$y=e^{-x}$')
    plt.plot(root, f(root), 'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.savefig("falsi_py.png")
    return "falsi_py.png"

def falsi_time(a,b,tol):
    eqa = 'np.exp(-x) -x'
    f = lambda x : eval(eqa)
    n_time = 10
    SETUP_CODE = '''from __main__ import falsi, f'''
    TEST_CODE = '''falsi(f, {}, {}, {})'''.format(a,b,tol)
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
#     sol = falsi(f,a,b,tol)
#     print('sol = ',sol)
#     falsi_time(a,b,tol)
#     falsi_plot(f,a,b,sol)