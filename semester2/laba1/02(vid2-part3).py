import matplotlib.pyplot as plt
import numpy as np

def my_graph(x, a, b, c):
    '''
    y = a*(2*x**4) + b*(x**2) + c
    '''
    return a*(2*x**4) + b*(x**2) + c

# plt.xkcd()
plt.style.use("seaborn-muted")

a = -5; b = 200 ; c = 100

left = -100; right = 0; step = .01
data_x = np.arange(left, right, step)
data_y = [my_graph(x, a, b, c) for x in data_x]    
plt.plot(data_x, data_y, color = "#66CCFF")

a = +10; b = 200 ; c = 100
left = 0; right = 100; step = .01
data_x = np.arange(left, right, step)
data_y = [my_graph(x, a, b, c) for x in data_x]    
plt.plot(data_x, data_y, color = "#FFCC00")

plt.title("График данной функции")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)
plt.axhline(lw = 2, color = "#FF6699")
plt.axvline(lw = 2, color = "#FF6699")
plt.show()