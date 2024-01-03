import math

def quadratic_equation_solver(a,b,c):
    #Returns a list of all the roots of a Quadratic Equation, false if there are no Real Roots.
    #Requires that 'a' cannot be equal to zero.
    if (((b*b)-(4*a*c))<0): return False
    x=((-b+math.sqrt((b*b)-(4*a*c)))/(2*a))
    y=((-b-math.sqrt((b*b)-(4*a*c)))/(2*a))
    if x==y: return [x]
    return [x,y]



#tests
print(quadratic_equation_solver(1,2,2))
print(quadratic_equation_solver(1,2,1))
print(quadratic_equation_solver(-1,2,1))
print(quadratic_equation_solver(-1,0,0))
print(quadratic_equation_solver(1,0,0))
