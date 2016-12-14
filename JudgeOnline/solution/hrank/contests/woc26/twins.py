'''
Created on 4 de dez de 2016

@author: C.Lucas
http://introcs.cs.princeton.edu/java/14array/PrimeSieve.java.html
https://www.hackerrank.com/contests/w26/challenges/twins

'''
from math import sqrt
numbers = []
def sieveErathostenes(sz = int(sqrt(1E9))):
    primes  = []
    numbers = [True] * ( sz + 1 )
    numbers[0], numbers[1] = [False, False]
    i = 2
    while (i*i <= sz):
        if(numbers[i]):
            j = i
            while(j*i <= sz):
                numbers[j*i] = False
                j+=1
        i+=1
    for i in range(0, len(numbers)):
        if(numbers[i]):
            primes.append(i)
    #print(len(primes))
    return primes


def sieve(sz = int(1E9)):
    i = 2
    p = []
    while(i*i <= sz):
        j = 2
        f = True
        '''
        procurar um valor j que seja multiplo de i
        se esse valor existir, ele sera no maximo igual a raiz quadrada de i
        ( j <= sqrt(i) ou j^2 <= i
        '''
        #while(j <= int(sqrt(i))):
        while(j*j <= i):
            if((i % j) == 0):
                f = False
                break
            j += 1
        if(f):
            p.append(i)
        i+=1
    return p

def rangeSieve(a, b):
    primes = []
    if( (a & 1) == 0):
        a+=1
    if(a < 3):
        primes.append(2)
    for x in range(a, b+1, 2):
        if(isPrimeSqrt(x)):
            primes.append(x)
    return primes

def countPrimesInterval(a, b):
    if( (a & 1) == 0 or a == 2):
        a+=1
    count = 0
    for x in range(a, b, 2):
        y = x+2
        if(isPrimeSqrt(x) and isPrimeSqrt(y) ):
            count += 1    
    return count
    
def isPrime(n):
    return numbers[n]

def isPrimeSqrt(n):
    if(n < 2):
        return False
    lim = int(sqrt(n))
    for i in range(2, lim+1):
        if(n % i == 0):
            return False
    return True

def readInts():
    from sys import stdin
    return [int(x) for x in stdin.readline().strip().split(" ")]

def run():
    a, b  = readInts()
    count = 0
    _min = min(a,b)
    _max = max(a,b)
    if(_min < 3):
        _min = 3
    elif( (_min & 1) == 0):
        _min += 1
    for i in range(_min, _max-1, 2):
        a, b = [i, i+2]
        if(isPrimeSqrt(a) and isPrimeSqrt(b) and (b-a) == 2):
            count +=1
    print(count)

def run2(): 
    a, b  = readInts()
    count = 0
    _min = min(a,b)
    _max = max(a,b)
    sieve = rangeSieve(_min, _max)
    if(len(sieve) > 1):
        for i in range(0, len(sieve)-1):
            a, b = [sieve[i], sieve[i+1]]
            if(b-a == 2):
                count += 1
    return count

def run3():
    primes  = sieveErathostenes()
    a, b    = readInts()
    if(b < a):
        aux = b
        b = a
        a = aux
    if(a == 1):
        a = 3    
    if(a & 1 == 0):
        a += 1
    # 'a' senore comecara no minimo do 3
    count, lastNumber = [0,0]
    for i in range(a, b+1, 2):
        j = 0
        p = primes[j]
        hasDivisors = False
        while(j < len(primes) and p*p <= i):
            if(i % p == 0):
                hasDivisors = True
                break
            p = primes[j]
            j += 1
        
        if(not hasDivisors):
            count += 1 if(i - lastNumber == 2) else 0
            lastNumber = i
    
    return count    

'''
1 1000000 = 8169
203 10001 = 190
999000000 1000000000 = 3063
793231275 793692317 = 1474

k = int(sqrt(1E9))
sieveErathostenes(k)
sieve(k)
'''
print(countPrimesInterval(1, 10))
print(countPrimesInterval(3, 13))
print(countPrimesInterval(1, 1000000))
print(countPrimesInterval(203, 10001))
print(countPrimesInterval(999000000, 1000000000))

print(run3())

if __name__ == '__main__':
    pass
'''
sieveErathostenes()
print(isPrimeSqrt(903))
'''

def getCurrentMilliseconds():
    # http://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
    from time import time
    tm = lambda : int(round(time() * 1000))
    return tm()     