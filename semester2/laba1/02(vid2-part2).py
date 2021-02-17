import matplotlib.pyplot as plt


def my_graph(x, a, b, c, d):
    return (a*(2*x**4) + b*(x**2) + c) / (x + d)

# plt.xkcd()
plt.style.use("seaborn-muted")
a = -5; b = 200 ; c = 100; d = -5
legend = "y = {}*(2*x**4) + {}*(x**2) + {}".format(a, b, c)
left = -100; right = 100; step = 0.8

data_x = []; data_y = []
pos_x = left
while pos_x <= right:
     try:
         pos_y = my_graph(pos_x, a, b, c, d)
         data_x.append(pos_x)
         data_y.append(pos_y)
     except:
         pass
     pos_x += step

plt.plot(data_x, data_y, lw = 3, color = "#66CCFF")

plt.grid(True)
plt.axhline(lw = 2, color = "#FF6699")
plt.axvline(lw = 2, color = "#FF6699")
plt.show()