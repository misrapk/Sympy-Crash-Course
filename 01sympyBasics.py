from sympy import Symbol, symbols, factor, expand

x = Symbol('x')

# v = x+x+1
# print(v)
# print(a.name)

# x = Symbol('x')
# y = Symbol('y')
# z = Symbol('z')

x, y, z = symbols('x, y, z')
# print(x+x + y**2 + z)

 #TODO: Expressions
 
 
# print(x*y + y*x)
# print((x+5) * (x+1))
# print(x**2  - y**2)
 
 
#factorization and Expanding
# expr = x**2 - y**2
# fExpr = factor(expr)

# print(expand(fExpr))


# expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
expr = (x+y)**4
print(expand(expr))

