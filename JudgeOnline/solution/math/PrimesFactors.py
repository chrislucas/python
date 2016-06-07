'''
Created on 7 de jun de 2016

@author: C.Lucas

Tentar resolver esse
https://www.urionlinejudge.com.br/judge/pt/problems/view/1398

Fermat's factorization method
https://en.wikipedia.org/wiki/Fermat%27s_factorization_method

Crivo de Eratóstenes com o tempo de trabalho linear
http://e-maxx.ru/algo/prime_sieve_linear

Fatoracao em primos
https://en.wikipedia.org/wiki/Fermat_primality_test
http://stackoverflow.com/questions/12756335/fast-prime-factorization-algorithm
https://en.wikipedia.org/wiki/Primality_test

Number Theory - 1
https://www.hackerearth.com/notes/number-th
https://people.eecs.berkeley.edu/~vazirani/algorithms/chap1.pdf

Math
https://www.topcoder.com/community/data-science/data-science-tutorials/mathematics-for-topcoders/

Fastest way to factor integers < 2^60
http://mathoverflow.net/questions/114018/fastest-way-to-factor-integers-260

http://www.codeproject.com/Tips/155308/Fast-Prime-Factoring-Algorithm
'''
import math

# http://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
def pFactors(n):
    f = []
    return None


mod = 131071
def f():
    number = '1011'
    for n in range(0, len(number)):
        if(number[n] == '1'):
            x = 1 << n % mod

if __name__ == '__main__':
    pass