def fibonacci_sequence(x):
    #Returns a list of the Fibonacci sequence from 0 up to <x> (inclusive).
    seq=[0,1]
    f_n=1
    if x==0: return [0]
    if x==1: return [0,1]
    while f_n<=x:
        seq.append(f_n)
        f_n=seq[-1]+seq[-2]
    return seq



#tests
print(fibonacci_sequence(0))
print(fibonacci_sequence(1))
print(fibonacci_sequence(2))
print(fibonacci_sequence(3))
print(fibonacci_sequence(4))
print(fibonacci_sequence(5))
print(fibonacci_sequence(6))
print(fibonacci_sequence(7))
print(fibonacci_sequence(8))
print(fibonacci_sequence(4180))
print(fibonacci_sequence(4181))
print(fibonacci_sequence(4182))

