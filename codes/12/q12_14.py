import numpy as np
import matplotlib.pyplot as plt
import os 

x1=np.linspace(-4*np.pi,4*np.pi,1000)

y=np.arccos(1/(x1))

plt.plot(x1 ,y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-5,5)
plt.title("Graph of $sec^{-1}x$")
plt.grid(True)
plt.show()

plt.savefig("q12_14.jpg")
image_path="q12_14.jpg"

os.system(f"termux-open '{image_path}'")

