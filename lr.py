import random
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import numpy

n = 100

x = np.array([i for i in range(n)])
bias=np.random.randn(100,1)*10

#y = np.array([15*i + 5 + random.randint(-100,100) for i in range(n)])
y = np.array([i + bias[i][0] for i in range(n)])

def get_slope_intercept(x,y):
    m = ((np.mean(x)*np.mean(y))-np.mean(x*y)) / (np.mean(x)**2 - np.mean(x*x))
    #m = np.sum((x-np.mean(x))*(y-np.mean(y)))/np.sum((x-np.mean(x))**2)
    b = np.mean(y) - m*np.mean(x)
    return m,b
def squared_err(y,y_pred):
    return np.sum((y-y_pred)**2)

def coeff_of_determonation(y,y_pred):
    y_mean = [np.mean(y) for i in y]
    se_y_reg = squared_err(y,y_pred)
    se_y_mean = squared_err(y,y_mean)
    return 1 - (se_y_reg/se_y_mean)

m,b = get_slope_intercept(x,y)
print("b1:{} and b0:{}".format(m,b))


pred_y = [m*x + b for x in range(n)]
print("Coeff of determination:",coeff_of_determonation(y,pred_y))

#u = (n*np.sum(x*y) - np.sum(x)*np.sum(y))
#l = sqrt((n*np.sum(x*x)-np.sum(x)**2)*(n*np.sum(y*y)-np.sum(y)**2))

R = np.sum((pred_y-np.mean(pred_y))**2)/np.sum((y-np.mean(y))**2)

print("R squared value(R^2):",R)

plt.scatter(x,y)
plt.plot(x,pred_y)

plt.show()