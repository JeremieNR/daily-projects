def collatz_conjecture(n):
    #Returns the result of Collatz Conjecture for n as a list of all numbers.
    #Requires n to be greater or equal to 1.
    lst=[]
    while not(n==1):
        if n%2==0:
            lst.append(n)
            n=n/2
        elif n%2==1:
            lst.append(n)
            n=3*n+1
    lst.append(n)
    return lst



#tests
print(collatz_conjecture(1))
print(collatz_conjecture(2))
print(collatz_conjecture(50))
print(collatz_conjecture(100))
print(collatz_conjecture(1000))
print(collatz_conjecture(989345275647))





#Fun fact: Every number inputed into the Collatz Conjecture up to (2^100000)-1 converges to 1.
