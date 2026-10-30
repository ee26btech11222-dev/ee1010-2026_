import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append('.')

from CoordGeo.line.funcs import line_gen

x = np.linspace(-3, 3, 1000)

y1 = (42 - 9*x) / 10
y2 = (14 - 9*x) / 10

pts1 = line_gen(np.vstack((x, y1))[:, :-1], np.vstack((x, y1))[:, 1:])
pts2 = line_gen(np.vstack((x, y2))[:, :-1], np.vstack((x, y2))[:, 1:])

plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="green")

plt.xlabel("x")
plt.ylabel("y")
plt.title("paralell lines")
plt.grid(True)

plt.show()
plt.savefig("parallel_lines.jpg")
image_path = "parallel_lines.jpg"

os.system(f"termux-open '{image_path}'")
