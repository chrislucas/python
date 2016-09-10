'''
Created on 6 de set de 2016

@author: chrislucas
'''

'''
https://en.wikipedia.org/wiki/Polite_number
http://crbonilha.com/pt/1-exercicios-aleatorios/#more-549
'''

'''
O numero de maneiras de se expressar N como uma soma de inteiros
consecutivos e igual ao numero de divisores impares de N

Sieve
http://introcs.cs.princeton.edu/java/14array/PrimeSieve.java.html

                    n     Primes <= n
 *  ---------------------------------
 *                 10               4   
 *                100              25  
 *              1,000             168  
 *             10,000           1,229  
 *            100,000           9,592  
 *          1,000,000          78,498  
 *         10,000,000         664,579  
 *        100,000,000       5,761,455  
 *      1,000,000,000      50,847,534 

'''
class Primes:

    def __init__(self, q):
        self.primes = []
        self.bools = [True] * (q+1)
        self.bools[0],  self.bools[1], = [False, False]
        
        # crivo
        i = 2
        while(i*i <= q):
            if(self.bools[i]):
                j = i+i
                while(j<=q):
                    self.bools[j] = False
                    j+=i
            i+=1
        
        for x in range(0, len(self.bools)):
            if(self.bools[x]):
                self.primes.append(x)        
        return

    def isprime(self, num):
        if len(self.bools) < num:
            return False
        return self.bools[num]
    
    def quantity(self):
        return len(self.primes)

primes = Primes(1000000)

print(primes.isprime(5))
print(primes.quantity())

if __name__ == '__main__':
    pass