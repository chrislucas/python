'''
Created on 10 de dez de 2016

@author: C.Lucas
'''

'''
3 13 = 3
1 1000000 = 8169
203 10001 = 190
999000000 1000000000 = 3063
793231275 793692317 = 1474
'''

from math import sqrt

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
    return primes

def readInts():
    from sys import stdin
    return [int(x) for x in stdin.readline().strip().split(" ")]

def countPrimesInterval(a, b):
    if( (a & 1) == 0 or a == 2):
        a+=1
    count = 0
    for x in range(a, b, 2):
        y = x+2
        if(isPrimeSqrt(x) and isPrimeSqrt(y) ):
            count += 1    
    return count

def isPrimeSqrt(n):
    if(n < 2):
        return False
    lim = int(sqrt(n))
    for i in range(2, lim+1):
        if(n % i == 0):
            return False
    return True

def run():
    a, b = readInts()
    if(b < a):
        aux = b
        b = a
        a = aux
    
    return countPrimesInterval(a, b)

print(run())

if __name__ == '__main__':
    pass