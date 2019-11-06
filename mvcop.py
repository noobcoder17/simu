#multivariable constrained optimization problem
from sympy import *
import numpy as np

X1 = Symbol('X1')
X2 = Symbol('X2')
S1 = Symbol('S1')
S2 = Symbol('S2')
L1 = Symbol('L1')
L2 = Symbol('L2')
#original equation 
print("Max Z = 10x1 - x1^2 + 10x2 - x2^2\n")
L = 10*X1-X1**2+10*X2-X2**2 - L1*(X1+X2+S1**2-14) - L2*(-X1+X2+S2**2-6)
LX1 = L.diff(X1)
LX2 = L.diff(X2)
LS1 = L.diff(S1)
LS2 = L.diff(S2)
LL1 = L.diff(L1)
LL2 = L.diff(L2)

LX1X1 = LX1.diff(X1)
LX2X1 = LX2.diff(X1)
LX1X2 = LX1.diff(X2)
LX2X2 = LX2.diff(X2)

print("Hessian matrix:")
print("[{} {}]".format(LX1X1,LX1X2))
print("[{} {}]".format(LX2X1,LX2X2))

M1 = int(LX1X1)
M2 = int(int(LX1X1)*int(LX2X2))-int(int(LX2X1)*int(LX1X2))

print("Minor 1:",M1)
print("Minor 2:",M2)

print("__Local Maxima is obtained__")

print("For Contrained solution L1 is non zero and L2 is non zero\n")

#when L(Lambda) is not zero
a = np.array([[1,1],[-1,1]])
b = np.array([14,6])
x = np.linalg.solve(a, b)
print("When lambda not zero then x1 = {} and x2 = {}".format(x[0],x[1]))
#when L(Lambda) is zero
c= np.array([[0,2],[2,0]])
d= np.array([10,10])
y = np.linalg.solve(c, d)
print("When lambda zero then x1 = {} and x2 = {}".format(y[0],y[1]))

print("\nThe solutions are:")
x1 = int(x[0])
x2 = int(x[1])
z1 = 10*x1-x1*x1+10*x2-x2*x2
print("When lambda not zero Z = "+str(z1))

x1 = int(y[0])
x2 = int(y[1])
z1 = 10*x1-x1*x1+10*x2-x2*x2
print("When lambda zero Z = "+str(z1))