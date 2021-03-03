from sympy import symbols, Symbol, pprint , expand, factor, simplify

x, y = symbols('x,y')

expr = x**2 + y**2

#x = 1 y =2

res = expr.subs({x:1, y:2})



# pprint(expr)
# print(res)
# pprint(expand(expr.subs({x:y+2})))


e = x*x + x*y + x*y + y*y
pprint(e)

eSub = e.subs({x:1-y})
pprint(eSub)
print(simplify(eSub))