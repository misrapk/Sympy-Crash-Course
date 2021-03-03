from sympy import Symbol, symbols, factor, expand, pprint, init_printing
x, y, z = symbols('x, y, z')


init_printing(order= 'rev-lex')
expr1 = x**3 + 3*x**2*y + 3*x*y**2 + y**3
expr2 = (x+y)**4
# print(expand(expr))

pprint(expand(expr2))
