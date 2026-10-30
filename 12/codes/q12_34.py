import numpy as np

A=([[5,-1,4],[2,3,5],[5,-2,6]])

B=([5,2,-1])

A_inv=np.linalg.inv(A)
X=np.linalg.inv(A) @ B

print("A_inv : ",A_inv)
print(X)
