import numpy as np

def f1(x):
    return np.exp(-x) - x

def f2(x):
    return x*np.exp(0.5*x) + 1.2*x - 5

def f3(x):
    return x**3 - x -1

def f4(x):
    return x**3 - x**2 -1

def f5(x):
    return x**2 -2

def f6(x):
    return np.exp((-x)**2) - x

def f7(x):
    return -x + 1 

def f8(x):
    return (1/5)**x - 2

def f9(x):
    return x**3 - 3*x**2 - 4*x + 5

def f10(x):
    return -(1/3)**x + 2

def getFunction(id):
    match id:
        case 1:
            return f1
        case 2:
            return f2
        case 3:
            return f3
        case 4:
            return f4
        case 5:
            return f5
        case 6:
            return f6
        case 7:
            return f7
        case 8:
            return f8
        case 9:
            return f9
        case 10:
            return f10

# ==================================

def df1(x):
    return -np.exp(-x) - 1

def df2(x):
    return np.exp(0.5*x) * (0.5*x+1) + 1.2

def df3(x):
    return 3*pow(x,2) - 1

def df4(x):
    return 3*pow(x,2) - 2*x

def df5(x):
    return 2*x

def df6(x):
    return np.exp(pow(x,2))*(2*x) - 1

def df7(x):
    return -1

def df8(x):
    return -np.log(5) * pow(1/5,x);

def df9(x):
    return 3*pow(x,2) - 6*x - 4

def df10(x):
    return np.log(3) * pow((1/3),x)

def getDiffFunction(id):
    match id:
        case 1:
            return df1
        case 2:
            return df2
        case 3:
            return df3
        case 4:
            return df4
        case 5:
            return df5
        case 6:
            return df6
        case 7:
            return df7
        case 8:
            return df8
        case 9:
            return df9
        case 10:
            return df10
