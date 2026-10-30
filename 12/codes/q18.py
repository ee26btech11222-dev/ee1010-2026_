import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os
import sys
sys.path.append('.')

from CoordGeo.line.funcs import line_gen

x1 = np.linspace(-3, 1, 1000)
k = float(input("enter the value of k :"))
y1 = k*(x1)**2 + 5

x2 = np.linspace(1, 4, 1000)
y2 = np.full_like(x2, 2)

pts1 = line_gen(np.vstack((x1, y1))[:, :-1], np.vstack((x1, y1))[:, 1:])
pts2 = line_gen(np.vstack((x2, y2))[:, :-1], np.vstack((x2, y2))[:, 1:])

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.xlabel("x")
plt.grid(True)
plt.ylabel("f(x)")
plt.title("Graph of f(x)")
plt.show()
plt.savefig("q12_18.jpg")
image_path = "q12_18.jpg"

os.system(f"termux-open '{image_path}'")
