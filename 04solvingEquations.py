from sympy import *

x = Symbol('x')
e = x**2-5-3

print(solve(e, dict=True))