def isprime(x):
    #Returns True if the given input is a prime number, False otherwise.
    #Requires x>=2
    lst=list(range(2,x))
    for n in lst:
        if x%n==0: return False
    return True




#tests
print(isprime(2)) #True
print(isprime(3)) #True
print(isprime(4)) #False
print(isprime(5)) #True
print(isprime(6)) #False
print(isprime(7)) #True
print(isprime(8)) #False
print(isprime(55)) #False
print(isprime(97)) #True
print(isprime(100)) #False
print(isprime(3907)) #True
