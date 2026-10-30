import numpy as np 
import matplotlib.pyplot as plt
import os 

x=np.linspace(-4*np.pi,4*np.pi,1000)

y=np.cos(x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("graph of cosx")
plt.grid(True)
plt.show()
plt.savefig("q5.jpg")
image_path="q5.jpg"
os.system(f"termux-open'{image_path}'")
