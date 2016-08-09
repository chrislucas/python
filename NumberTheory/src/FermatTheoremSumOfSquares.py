'''
Created on 3 de jul de 2016



@author: C.Lucas
https://brilliant.org/wiki/fermats-sum-of-two-squares-theorem/?utm_medium=social&utm_source=facebook&utm_campaign=fb_posts_07022016&utm_content=ww_fermats_sum_of_two_squares_theorem#fermats-theorem-on-the-sum-of-two-squares
'''
from sys import stdout

from datetime import datetime
#from sympy.mpmath.libmp.libintmath import isprime
from math import ceil, sqrt, floor

class Eratosthenes:
    def __init__(self, n):
        self.primes = []
        self._list = [True] * n
        self._list[0] = False
        self._list[1] = False
        for i in range(2, n):
            if(self._list[i]):
                j = i*i
                self.primes.append(i)
                while j < n:
                    self._list[j] = False
                    j += i
        self.quantity = len(self.primes)
        
    def isPrime(self, n):
        return self._list[n]
    
    def getPrimes(self):
        stdout.write("%d\n" % (self.quantity))
        #for i in self.primes:
            #stdout.write("%d\n" % (i))
    
    '''
    http://pontodeacumulacao.blogspot.com.br/2012/01/primos-que-sao-soma-de-quadrados.html
    Testando a ideia dess blog
    '''
    def isFactorTwoSquares(self, prime):
        if(prime < self.quantity and Eratosthenes.isPrime(prime)):
            # nehum numero primo que quando dividido por quatro deixa
            # resto 3 pode ser expresso numa soma de 2 quadrados
            # LOUCARA HEIN
            return False if prime % 4 == 3 else True
        return False


'''
Fermat's factorization method
https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
https://pt.wikipedia.org/wiki/M%C3%A9todo_de_fatora%C3%A7%C3%A3o_de_Fermat
'''
# N deve ser impar
def fermatFactor(n):
    a = ceil(sqrt(n))
    bb = a*a - n
    if(bb <= 1):
        return []
    while not isSquare(bb):
        a += 1
        bb = a*a-n
    #return a - sqrt(bb)
    b = int(sqrt(bb))
    c = a + b
    d = a - b
    return [a, b, c, d] 

def isSquare(n):
    rn = floor(sqrt(n))
    return n == rn*rn

'''
http://burningmath.blogspot.com.br/2013/09/how-to-check-if-number-is-perfect-square.html
http://www.trans4mind.com/personal_development/mathematics/numberTheory/fermatSieve.htm#Perfect_Squares_Modulo_10
'''
def otherIsSquare(n):
    return n % 16 == 0 or n % 16 == 1 or  n % 16 == 4 or n % 16 == 9
    
def runSieve():
    S = datetime.now().microsecond        
    sieve = Eratosthenes(1000000)
    E = datetime.now().microsecond
    stdout.write("%f\n" % ((E-S)/100000) )
    _list = [3,5,7,11,13,17,19,23,29,31,37,41,2017,7919]
    for num in _list:
        stdout.write("%s %d\n" % (sieve.isFactorTwoSquares(num), num) )
 
#runSieve()  
print( (fermatFactor(101)) )


   
if __name__ == '__main__':
    pass