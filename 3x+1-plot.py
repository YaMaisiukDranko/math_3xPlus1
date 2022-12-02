import matplotlib.pyplot as plt
import numpy as np

num = 7
x = np.ndarray([num])
y = np.ndarray([num])


def plot():
    global num
    global x
    global y
    while num != 1:  # Use while num != 1
        # Rules:
        if num % 2 == 0:  # Check parity
            num = num / 2
            print(int(num))
            y = np.append(y, num)
            x = np.append(x, 1)

        elif num % 2 != 0:
            num = num * 3 + 1
            print(int(num))
            y = np.append(y, num)
            x = np.append(x, 1)

plot()

print(x, y)
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.scatter(x, y, vmin=0, vmax=100)
ax.set(xlim=(0, 100), xticks=np.arange(1, 8),
       ylim=(0, 100), yticks=np.arange(1, 8))
plt.show()


