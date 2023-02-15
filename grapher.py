import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
interval = 4
sum = 0

for i in range(20):
    x.append(i)
    y.append(sum + interval)
    sum += interval
    interval += 1

print(x, y)
plt.plot(x, y)
plt.show()