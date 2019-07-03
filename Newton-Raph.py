from numpy import *

def f(x):
    y = x**4 - 10*(x**3) + 3*(x**2) + x + 23
    return y
def Df(x) :
    z = 4*(x**3) - 30*(x**2) + 6*x + 1
    return z

P0 = float(input("please insert the initial aproximation: "))
Err = float(input("Insert the tolerable error: "))
N = int(input("Number of iterations:  "))
i = 0
while i < N :
    P = P0 - (f(P0)/Df(P0))
    if abs(P - P0) < Err :
        print(P)
    i = i+1
    P0 = P
print ("The method succeed until ", N, "Iterations.")
    