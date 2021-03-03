from sympy import Symbol, pprint, init_printing

def seriesPrint(n, val):
    
    init_printing(order = 'rev-lex')
    x = Symbol('x')
    
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
        
    pprint(series)
    
    sValue = series.subs({x: val})
    print("value of series at {0} : {1}".format(val, sValue))
    
    
if __name__ == '__main__':
    n = input("Enter the value of n: ")
    x = input("enter the value of x: ")
    seriesPrint(int(n), float(x))
    