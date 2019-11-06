import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline


'exec(%matplotlib inline)'

# Construct lines
# x > 0
# x = np.linspace(-10, 60, 200)
# y1 = (200-5*x)/4.0
# y2 = (150-3*x)/5.0
# y3 = (100-5*x)/4.0
# y4 = (x*0)+0
# y5 = (80-8*x)/4.0

x = np.linspace(-10, 60, 200)
y1 = (50 - 5*x)/10
y2 = (16 - 8*x)/2
y3 = (3*x - 6)/2
y4 = (x*0)+0

plt.plot(x, y1, label=r'$y\geq2$')
plt.plot(x, y2, label=r'$2y\leq25-x$')
plt.plot(x, y3, label=r'$4y\geq 2x - 8$')
plt.plot(x, y4, label=r'$y\leq 2x-5$')
plt.xlim((0, 10))
plt.ylim((-3, 8))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')


# Make plot
# plt.plot(x, y1, label=r'$4y\geq 200-5x$')
# plt.plot(x, y2, label=r'$5y\leq 150-3x$')
# plt.plot(x, y3, label=r'$4y\geq 100-5x$')
# plt.plot(x, y4, label=r'$y\geq 0$')
# plt.plot(x, y5, label=r'$4y\geq 80-8x$')
# plt.xlim((0, 50))
# plt.ylim((0, 50))
# plt.xlabel(r'$x$')
# plt.ylabel(r'$y$')

# Fill feasible region
y5 = np.minimum(y1, y3)
y6 = np.maximum(y2, y4)
plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
Z = 0
# for _ in range():
A = np.array([[5,10],[8,2]])
B = np.array([50,16])
C = np.linalg.solve(A,B)
Z = max(100*C[0] + 60*C[1],Z)
#
# A = np.array([[5,4],[0,0]])
# B = np.array([0,0])
# C = np.linalg.solve(A,B)
# Z = max(300*C[0] + 400*C[1],Z)

print(C)
print(Z)

plt.show()
