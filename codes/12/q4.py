import numpy as np
import matplotlib.pyplot as plt
import os 

# f(x) = (x - 1) / (x * (x^2 - 1)) 

# Generate x ranges avoiding asymptotes
x1 = np.linspace(-2, -1.01, 1000)
x2 = np.linspace(-0.99, -0.01, 1000)
x3 = np.linspace(0.01, 2, 1000)

def f(x):
    return 1 / (x * (x + 1))

# Plot continuous branches
plt.plot(x1, f(x1),color='black')
plt.plot(x2, f(x2),color='black')
plt.plot(x3, f(x3),color='black')
plt.ylim(-10,10)

#there is a point of discontinuity at x=1
plt.scatter([1],[0.5],color='red',edgecolor='black')
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title(r'Graph of $f(x) = \frac{x-1}{x(x^2-1)}$')
plt.grid(True)
plt.show()
plt.savefig("q4.jpg")
image_path="q4.jpg"
os.system(f"termux-open '{image_path}'")
