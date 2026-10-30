import numpy as np
import os
import matplotlib.pyplot as plt

# Define range for x and polynomial p(x)
x = np.linspace(-3, 3, 500)
y = 2*x**4 - x**3 - 11*x**2 + 5*x + 5

# All zeros (roots)
roots = [-np.sqrt(5), -0.5, 1, np.sqrt(5)]
root_labels = [r'$-\sqrt{5}$', r'$-\frac{1}{2}$', '$1$', r'$\sqrt{5}$']

plt.figure(figsize=(9, 5.5))

# Plot polynomial curve
plt.plot(x, y, color='black')

# Reference axes
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')

# Add text labels for each root (without red dots)
for root, label in zip(roots, root_labels):
    offset = 1.5 if root in [-0.5, 1] else -3.5
    plt.text(root, offset, label)

# Plot formatting
plt.title(r'Graph of $p(x) = 2x^4 - x^3 - 11x^2 + 5x + 5$ and its Zeros', fontsize=13)
plt.xlabel('x', fontsize=12)
plt.ylabel('p(x)', fontsize=12)
plt.ylim(-15, 20)
plt.grid(True)

plt.show()
plt.savefig("q38.jpg")

image_path="q38.jpg"
os.system(f"termux-open '{image_path}'")
