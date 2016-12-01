'''
Created on 30 de nov de 2016

@author: C.Lucas
'''



if __name__ == '__main__':
    pass

# https://www.hackerrank.com/contests/w26/challenges/best-divisor

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
    divs = divisors(n)
    ans = 1
    if(len(divs) > 1):
        ans = fx(divs[0], divs[1])
        for idx in range(2, len(divs)-1):
            prev = fx(divs[idx], divs[idx+1])
            ans = fx(prev, ans)
    return ans

#print(*divisors(12))
n = readInt()
print(solver(n))