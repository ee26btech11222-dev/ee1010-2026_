from sympy import Eq, Symbol, solve

# det_A: determinant of matrix A, |A|
n = 3
det_A = Symbol("det_A")

# Equation derived from taking determinant on both sides of A^2 = 3A:
# |A^2| = |3A|
# |A|^2 = 3^n * |A|
equation = Eq(det_A**2, (3**n) * det_A)

# Solve for |A|
solutions = solve(equation, det_A)

non_zero_sol= []
for sol in solutions:
    if (sol != 0):
        non_zero_sol.append(sol)

print(f"The value of |A| is: {non_zero_sol}")

