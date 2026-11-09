import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os
import sys
sys.path.append('.')

from CoordGeo.line.funcs import line_gen_num

x1 = np.linspace(-3, 1, 1000)
k = float(input("enter the value of k :"))
y1 = k*(x1)**2 + 5

x2 = np.linspace(1, 4, 1000)
y2 = np.full_like(x2, 2)

# Endpoints A and B for both segments
A1 = np.array([-3, k*(-3)**2 + 5]).reshape(-1, 1)
B1 = np.array([1, k*(1)**2 + 5]).reshape(-1, 1)

# Generate points using CoordGeo line_gen_num
pts1 = line_gen_num(A1, B1, 1000)

plt.plot(x1, y1)
plt.plot(x2, y2)

# Plot endpoints A and B
plt.scatter([A1[0, 0], B1[0, 0]], [A1[1, 0], B1[1, 0]], color='red')

plt.text(A1[0, 0], A1[1, 0], '  A1', verticalalignment='bottom')
plt.text(B1[0, 0], B1[1, 0], '  B1', verticalalignment='bottom')

plt.xlabel("x")
plt.grid(True)
plt.ylabel("f(x)")
plt.title("Graph of f(x)")
plt.show()
plt.savefig("q12_18.jpg")
image_path = "q12_18.jpg"

os.system(f"termux-open '{image_path}'")
