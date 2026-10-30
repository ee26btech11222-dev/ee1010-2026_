import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os

x1=np.linspace(-3,1,1000)
k=float(input("enter the value of k :"))
y1=k*(x1)**2 +5

x2=np.linspace(1,4,1000)
y2=np.full_like(x2,2)

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlabel("x")
plt.grid(True)
plt.ylabel("f(x)")
plt.title("Graph of f(x)")
plt.show()
plt.savefig("q12_18.jpg")
image_path="q12_18.jpg"

os.system(f"termux-open '{image_path}'")
