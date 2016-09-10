'''
Created on 10 de set de 2016

@author: chrislucas
'''

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1568

from math import sqrt
from sys import stdin, stdout

def criveErathostenes(n):
    q = n #int(sqrt(n) + 1)
    bools = [True] * (q+1)
    bools[0], bools[1], = [False, False]
    primes = []
    # crivo
    i = 2
    while(i <= q):
        if(bools[i]):
            primes.append(i)
            j = i*i
            while(j<=q):
                bools[j] = False
                j+=i
        i+=1
    return primes  

def factorization(n):
    factors = {}
    limit = sqrt(n) + 1
    prime = 2
    while(n > 1 and prime < limit):
        '''
            explicacao rapida: so sera inclusos
            no mapa 'factors' numeros primos
            A prova completa disso e explicada no arquivo 'Fatorization.py'
            Um numero composto pode ser escrito de uma unica forma pela soma
            de numeros primos (Teorema fundamental da aritmetica)
            Um numero D composto e  formado por p numero(s) primo(s) menores que D
            logo se tivessemos numeros compostos em factors' eles ja deveriam ter sido
            dividios por primos menores que ele
        '''
        while(n%prime==0):
            if(prime in factors):
                factors[prime] += 1
            else:
                factors[prime] = 1
            n //= prime
        prime+=1
    '''
    caso n torne-se um primo (exemplo 121/11 = 11)
    '''
    if(n > 1):
        if(n in factors):
            factors[n] += 1
        else:
            factors[n] = 1
    return factors

'''
TLE
'''
def solver1(n):
    factors = factorization(n)
    ans = 0
    if(hasattr(factors, '__iter__') and len(factors) > 0):
        #for k in factors.keys():
        #for v in factors.values():
        ans = 1
        for k, v in factors.items():
            if(k == 2):
                continue
            ans *= (v+1)
    return ans

def solver2(n, primes):
    if(n == 0):
        return n
    factors = {}
    limit   = len(primes)
    count   = 0
    p = primes[count]
    while(n > 1 and count < limit and p*p <= n):
        p = primes[count]
        while(n%p == 0):
            if(p in factors):
                factors[p] += 1
            else:
                factors[p] = 1
            n //= p
        count += 1
    # caso n seja primo
    if(n > 1):
        if(n in factors):
            factors[n] += 1
        else:
            factors[n] = 1
    
    ans = 1
    for k, v in factors.items():
        if(k == 2):
            continue
        ans *= (v+1)

    return ans

def run():
    limits = [10000001, 9E12+1, 10000, 1000000]
    # comentei a parte do codigo sqrt(n) na funcao criveErathostenes
    primes = criveErathostenes(limits[3])
    while True:
        try:
            n = int(stdin.readline())
            #ans = solver1(n)
            ans = solver2(n, primes)
            stdout.write("%d\n" % (ans))
        except:
            break
run()

if __name__ == '__main__':
    pass