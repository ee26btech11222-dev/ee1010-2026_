import numpy as np
import matplotlib.pyplot as plt
import subprocess
import sys
sys.path.append('.')

from CoordGeo.line.funcs import line_gen

# Define the range for x
x = np.linspace(-1, 8, 500)
y = (x**2) * np.exp(-x)

# Generate line points matrix using CoordGeo line_gen
pts = line_gen(np.vstack((x, y))[:, :-1], np.vstack((x, y))[:, 1:])

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("graph of $x^2e^{-x}$")

plt.grid(True)

plt.show()
plt.savefig("12_3 graph.jpg")
image_path = "12_3 graph.jpg"
subprocess.run(["xdg-open", image_path])
