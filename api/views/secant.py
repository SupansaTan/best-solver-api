# https://personal.math.ubc.ca/~pwalls/math-python/roots-optimization/secant/

import numpy as np
import matplotlib.pyplot as plt
import timeit

def secant(f,a,b,N=20):
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

def secant_plot(f,a,b,root):
    x = np.linspace(a,b, 1000)
    f1 = f(x)
    plt.plot(x, f1, '-', label=r'$y=e^{-x}$')
    plt.plot(root, f(root), 'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

def secant_time(a,b):
    n_time = 10
    SETUP_CODE = '''from __main__ import secant, f'''
    TEST_CODE = '''secant(f, {}, {})'''.format(a,b)
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

#     a,b = 0.4,0.6
#     sol = secant(f,a,b)
#     print('sol = ', sol)
#     secant_time(a,b)
#     secant_plot(f,a,b,sol)