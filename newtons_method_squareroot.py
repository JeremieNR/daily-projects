def newtons_method_squareroot(n,m):
    #Returns the approximate squareroot of 'n' (within 'm') by using Newtons Method.
    x=n
    r=0.5*(x+(n/x))
    while True:
        r=0.5*(x+(n/x))
        if (abs(r-x)<m):
            return r
        x=r




#Tests
print(newtons_method_squareroot(1,0.0001))
print(newtons_method_squareroot(2,0.0001))
print(newtons_method_squareroot(3,0.0001))
print(newtons_method_squareroot(4,0.0001))
print(newtons_method_squareroot(5,0.0001))
print(newtons_method_squareroot(6,0.0001))
print(newtons_method_squareroot(9,0.0001))
print(newtons_method_squareroot(16,0.0001))
print(newtons_method_squareroot(25,0.0001))
print(newtons_method_squareroot(40,0.0001))
print(newtons_method_squareroot(4034643,0.0001))
