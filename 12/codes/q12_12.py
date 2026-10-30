import sympy as sp
import numpy as np

x=sp.Symbol('x')

left_det=sp.Matrix([[2*x ,-9],[-2,x]]).det()

right_det=sp.Matrix([[-4,8],[1,-2]]).det()

equation=sp.Eq(left_det,right_det)

solutions=sp.solve(equation,x)

print(f"values of x :{solutions}")
