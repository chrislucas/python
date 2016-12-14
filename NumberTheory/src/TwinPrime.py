'''
Created on 10 de dez de 2016

@author: C.Lucas

https://en.wikipedia.org/wiki/Twin_prime
'''

'''
Testando uma solucao de autoria de 'zzkoza'
https://www.hackerrank.com/contests/w26/challenges/twins/forum
'''
def Solution(m, n):
    lim = 33000
    bit = [True] * lim
    bit[0] = False
    bit[1] = False
    if(n == 1):
        n+=1
    for x in range(3, lim, 2):
        if( bit[x/2] ):
            for y in range(x/2, lim, x):
                bit[y] = False
    primes = []
    for x in range(0, lim):
        if(bit[x]):
            primes.append(x*2+1)
            
    seq = [False] * 1000001
    for x in range(0, len(primes)):
        p = primes[x]
        s = m - m % p
        if(s < m):
            s += p
        if(s == p):
            s = 2*p
        while(s <= n):
            seq[s-m] = True
            s += p
            
    count = 0
    for x in range(2, (m-n)):
        if(not seq[x] and not seq[x-2]):
            count += 1
    return count


print(Solution(1, 10))
print(Solution(999000000, 1000000000))

if __name__ == '__main__':
    pass