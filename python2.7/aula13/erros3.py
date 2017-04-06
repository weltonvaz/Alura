from sympy.ntheory import isprime
for x in range(74207283,74207999,2):
    if isprime(x) == True:
        a = bin(x)
        b = a.count('0')-1
        c = a.count('1')
        d = b+c
        if d == 27:
            print(x)
            
    
