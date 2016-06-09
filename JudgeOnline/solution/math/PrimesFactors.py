'''
Created on 7 de jun de 2016

@author: C.Lucas

Tentar resolver esse
https://www.urionlinejudge.com.br/judge/pt/problems/view/1398

Fermat's factorization method
https://en.wikipedia.org/wiki/Fermat%27s_factorization_method

Crivo de Eratostenes com o tempo de trabalho linear
http://e-maxx.ru/algo/prime_sieve_linear

Fatoracao em primos
https://en.wikipedia.org/wiki/Fermat_primality_test
http://stackoverflow.com/questions/12756335/fast-prime-factorization-algorithm
https://en.wikipedia.org/wiki/Primality_test

Number Theory-1
https://www.hackerearth.com/notes/number-th
https://people.eecs.berkeley.edu/~vazirani/algorithms/chap1.pdf

Math
https://www.topcoder.com/community/data-science/data-science-tutorials/mathematics-for-topcoders/

Fastest way to factor integers < 2^60
http://mathoverflow.net/questions/114018/fastest-way-to-factor-integers-260

http://www.codeproject.com/Tips/155308/Fast-Prime-Factoring-Algorithm
'''

from math import sqrt, log10


'''
https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
'''
def fermatFactorization(n):
    f = []

    return f

def log(lg, base):
    return log10(lg) / log10(base)

def decToBin(num):
    sz = int(log(num, 2)) + 1
    _bin = [None] * sz
    for i in range(sz-1, -1, -1):
        _bin [i] = True if (num & 1) == 1 else False
        num >>= 1
    return _bin

def expmodular(b, e, mod):
    if(e == 0):
        return 1
    elif(e < 0):
        e = -e
        b = 1/b
    elif(e == 1):
        return b
        
    _bin = decToBin(e)
    ans = 1
    for bit in (_bin):
        ans = (ans * ans) % mod
        if(bit):
            ans = (ans * b) % mod
    return ans;

mod = 131071
def f():
    number = [
        '1010'    #10
        ,'1010101'    #85
        ,'11111111111111111000' #1048568
        ,'1111111111111111100' # 524284
    ]
    
    '''
    https://acmproblemsolver.wordpress.com/2012/08/07/solution-of-acm-uva-10176-ocean-deep-make-it-shallow-3/
    https://acmproblemsolver.wordpress.com/2012/08/07/solution-of-acm-uva-10551-basic-remains/
    '''

    sz = len(number[2]) - 1
    x = 0
    for n in range(0, sz):
        if(number[2][n] == '1'):
            #x = expmodular(2, sz-n, mod) % mod
            x = x << 1
            x = x + 1
            x = x % mod
    print(x)
f()

if __name__ == '__main__':
    pass