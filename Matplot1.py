import numpy as np

def f(x):
    return np.exp(x)

def g(y):
    return y**2

def h(z):
    a= f(z)
    b= g(a)
    return b

print(h(4))