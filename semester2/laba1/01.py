

x = np.linespace(-3 , 3, 50)
y = (x**2 + y**2) / 3*x

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()