import numpy as np
import matplotlib.pyplot as plt
import subprocess
import sys
sys.path.append('.')

from CoordGeo.line.funcs import line_gen_num

# Define the start and end points for the segment
A = np.array([-1, (-1)**2 * np.exp(-(-1))]).reshape(-1, 1)
B = np.array([8, (8)**2 * np.exp(-8)]).reshape(-1, 1)

# Generate line points using CoordGeo line_gen_num
pts = line_gen_num(A, B, 500)

# Mark points A and B with dots
plt.scatter([A[0, 0], B[0, 0]], [A[1, 0], B[1, 0]], color='red', zorder=5)

# Label points A and B on the plot
plt.text(A[0, 0], A[1, 0], '  A (-1, e)')
plt.text(B[0, 0], B[1, 0], '  B (8, 64e⁻⁸)')

# Define continuous range for smooth function plotting
x = np.linspace(-1, 8, 500)
y = (x**2) * np.exp(-x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("graph of $x^2e^{-x}$")

plt.grid(True)

plt.show()
plt.savefig("12_3 graph.jpg")
image_path = "12_3 graph.jpg"
subprocess.run(["xdg-open", image_path])
