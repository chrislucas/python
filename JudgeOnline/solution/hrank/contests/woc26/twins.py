'''
Created on 4 de dez de 2016

@author: C.Lucas
http://introcs.cs.princeton.edu/java/14array/PrimeSieve.java.html
https://www.hackerrank.com/contests/w26/challenges/twins

'''

sz = 10000000
numbers = [] #[True] * (sz+1)

def sieveErathostenes():
    primes  = []
    numbers = [True] * (sz+1)
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
    
def isPrime(n):
    return numbers[n]


def isPrimeSqrt(n):
    if(n < 2):
        return False
    from math import sqrt
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
    
def getCurrentMilliseconds():
    # http://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
    from time import time
    tm = lambda : int(round(time() * 1000))
    return tm()        

#sieveErathostenes()
#print(isPrimeSqrt(903))
'''
1 1000000 = 8169
203 10001 = 190
999000000 1000000000 = 3063
'''
#run()
print(run2())

if __name__ == '__main__':
    pass