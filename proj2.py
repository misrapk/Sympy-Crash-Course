from sympy import expand, symbols, sympify,pprint
from sympy.core.sympify import SympifyError

def product(e1, e2):
    
    prod = expand(e1*e2)
    
    pprint(prod)
    
    
if __name__ == '__main__':
    e1 = input("Enter First Equation: ")
    e2 = input("Enter Second Equation: ")
    
    #TODO: convert to expression
    try:
        e1 = sympify(e1)
        e2 = sympify(e2)
    except SympifyError:
        print("INvalid INput")
        
    else:
        product(e1, e2)
    

