import matplotlib.pyplot as plt
import numpy as np
import os 

# Take value of k as user input
k = float(input("Enter the value of k: "))

# Define range for x
x = np.linspace(-5, 5, 1000)
y = 2 * (x**2) + k * x + 2

# Create plot
plt.ylim(-10,10)
plt.plot(x, y,color="red")

# Reference x and y axes


# Formatting
plt.title(f'Graph of Quadratic Equation for $k = {k}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

plt.show()
plt.savefig("q1.jpg")
image_path="q1.jpg"

os.system(f"termux-open '{image_path}'")
