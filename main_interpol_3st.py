import numpy as np
import interpolacja as it
import matplotlib.pyplot as plt

data = np.array([[1., 3.],[2., 1.],[3.5, 4.],[5., 0.],[6., .5],[9., -2.],[9.5, -3.]])

lin_start = -1
lin_end = 12
lin_step = 1000
interpol = it.Interpolacja(data)
x = np.linspace(lin_start, lin_end, lin_step)
a = np.zeros(data.shape[0] - 1)
b = np.zeros(data.shape[0] - 1)
c = np.zeros(data.shape[0] - 1)
h = interpol.h_i
z = interpol.z_i()

for i in range(data.shape[0] - 1):
    a[i] = (1/(6 * h[i])) * (z[i+1] - z[i])
    b[i] = z[i]/2
    c[i] = ((-1 * h[i])/6) * (z[i+1] + (2 * z[i])) + 1/h[i] * (data[i+1, 1] - data[i, 1])

S = np.zeros(x.shape[0])

for i in range(data.shape[0] - 1):
    S += (data[i, 1] + (x - data[i, 0]) * (c[i] + (x - data[i, 0]) * (b[i] + (x - data[i, 0]) * a[i]))) * ((x < data[i + 1, 0]) * (x >= data[i, 0]))

S += (data[0, 1] + (x - data[0, 0]) * (c[0] + (x - data[0, 0]) * (b[0] + (x - data[0, 0]) * a[0]))) * ((x < data[0, 0]) * (x >= lin_start))
S += (data[-1, 1] + (x - data[-1, 0]) * (c[-1] + (x - data[-1, 0]) * (b[-1] + (x - data[-1, 0]) * a[-1]))) * ((x < lin_end) * (x >= data[-1, 0]))
S[-1] += (data[-1, 1] + (x[-1] - data[-1, 0]) * (c[-1] + (x[-1] - data[-1, 0]) * (b[-1] + (x[-1] - data[-1, 0]) * a[-1])))

plt.plot(data[:, 0], data[:, 1], marker='*')
plt.plot(x, S)
plt.show()

print(interpol.h_and_b()['h'])
print(interpol.h_and_b()['b'])
print(interpol.u_i())
print('===============')
print(interpol.z_i())
