import matplotlib.pyplot as plt
import numpy as np

num = 3
y = np.ndarray([num])
i = num


def plot():
    global num
    global x
    global y
    global i
    while num != 1:  # Use while num != 1
        # Rules:
        if num % 2 == 0:  # Check parity
            num = num / 2
            print(int(num))
            i += 1
            y = np.append(y, num)

        elif num % 2 != 0:
            num = num * 3 + 1
            print(int(num))
            i += 1
            y = np.append(y, num)


# x = np.append(x, y.max())
plot()
y = y[y != 0]
x = np.arange(1, len(y) + 1)

print(x, y)
# plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set(xlim=(0, len(x)),
       ylim=(0, y.max()))
ax.set_xlabel('Actions')
ax.set_ylabel('Number')
ax.set_box_aspect(1)
plt.show()


