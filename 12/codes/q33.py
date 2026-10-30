import numpy as np
import matplotlib.pyplot as plt
import os

x=np.linspace(0,8,1000)
x1=np.linspace(0.4,1000)

y_circ_upper=np.sqrt(8*x-x**2)
y_circ_lower=-y_circ_upper

y_para_upper=np.sqrt(4*x)
y_para_lower =-y_para_upper

plt.plot(x,y_circ_upper,color="green")
plt.plot(x,y_circ_lower,color="green")

plt.plot(x,y_para_upper,color="blue")
plt.plot(x,y_para_lower,color="blue")

plt.xlabel("x")
plt.ylabel("y")
plt.scatter([0,4,4],[0,4,-4],color="red")
plt.title("curves $x^2+y^2=8x $ and $y^2=4x$")
plt.grid(True)
plt.show()
plt.savefig("q34.jpg")
image_path="q34.jpg"
os.system(f"termux-open '{image_path}'")
