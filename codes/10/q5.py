import numpy as np
import matplotlib.pyplot as plt
import os

# Points & Circle setup
R = 2
O, B = np.array([0, 0]), np.array([0, -R])
A = np.array([R * np.cos(np.radians(-190)), R * np.sin(np.radians(-190))])



# 1. Circle & Tangent Line
plt.gca().add_patch(plt.Circle(O, R, color='black', fill=False, lw=1.5))
plt.annotate('_', xy=(3, -R), xytext=(-3, -R),arrowprops=dict(lw=0.5))

# 2. Triangle Lines (OA, OB, AB)
plt.plot([O[0], A[0], B[0], O[0]], [O[1], A[1], B[1], O[1]])

# 3. Angle Arc (100°)
angles = np.radians(np.linspace(-190, -90, 30))
plt.plot(0.5 * np.cos(angles), 0.5 * np.sin(angles), 'k-', lw=1)
plt.text(-0.3, -0.6, r'$100^\circ$', fontsize=10)

# 4. Labels & Points
labels = {'O': (O, (0.1, 0.1)), 'A': (A, (-0.3, 0)), 'B': (B, (0, -0.3)), 'P': ((-2.8, -R), (0, -0.3)), 'Q': ((2.8, -R), (0, -0.3))}

# Styling
plt.scatter([O[0], A[0], B[0]], [O[1], A[1], B[1]])

plt.gca().set_aspect('equal')
plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)
plt.axis('off')

plt.tight_layout()
plt.show()
plt.savefig("q2.jpg")
image_path=
