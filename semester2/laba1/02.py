import matplotlib.pyplot as plt
import numpy as np

def my_graph(x, a, b, c):
    '''
    y = a*(2*x**4) + b*(x**2) + c
    '''
    return a*(2*x**4) + b*(x**2) + c


a = -5; b = 200 ; c = 100
legend = "y = {}*(2*x**4) + {}*(x**2) + {}".format(a, b, c)
left = -100; right = 100; step = .1

data_x = np.arange(left, right, step)
data_y = [my_graph(x, a, b, c) for x in data_x]    

plt.plot(data_x, data_y)
plt.title("График данной функции")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.legend([legend])
plt.grid(True)
plt.axhline()
plt.axvline()
plt.show()