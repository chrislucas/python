'''
Created on 30 de nov de 2016

@author: C.Lucas
'''



if __name__ == '__main__':
    pass

# https://www.hackerrank.com/contests/w26/challenges/best-divisor
# DONE

from sys import stdin

def readInt():
    return int(stdin.readline().strip())

def summation(n):
    acc = 0
    while(n > 0):
        acc += n%10
        n//=10
    return acc


def divisors(n):
    divs = [];
    divs.append(1)
    div = 2
    while(div <= n):
        if(n % div == 0):
            divs.append(div)
        div += 1
    return divs

# funcao solicitada no problema
def fx(a, b):
    sumA = summation(a)
    sumB = summation(b)
    if(sumA > sumB):
        ans = a
    elif(sumB > sumA):
        ans = b
    else:
        ans = min(a, b)
    return ans

def solver(n):
    ans = 1
    if(n > 1):
        divs = divisors(n)
        ans = fx(divs[0], divs[1])
        for idx in range(1, len(divs)-1):
            prev = fx(divs[idx], divs[idx+1])
            ans = fx(prev, ans)
    return ans

def solver2(n):
    '''
    Numeros impares nao possui divisores pares
    '''
    #from math import sqrt
    #limit = int(sqrt(n))
    step    = 2 if((n & 1) == 1) else 1
    start   = 3 if((n & 1) == 1) else 2
    ans     = 1
    for x in range(start, n+1, step):
        if((n % x) == 0):
            ans = fx(ans, x)

    return ans        
    
#print(*divisors(12))
n = readInt()
print(solver(n))