'''
Created on May 5, 2016

@author: christoffer
'''
from sys import stdout
from cmath import sqrt

'''
Aprendendo a usar o Yield
https://diofeher.wordpress.com/2011/04/12/explicando-iterables-generators-yield-no-python/
http://www.python-course.eu/python3_generators.php
'''

def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i<n:
        yield a
        a , b = b, a+b 
        i = i + 1

def iterator(it):
    for i in it:
        stdout.write("%d " % (i))

def isIterator(it):
    if(
        hasattr(it, '__iter__') and
        hasattr(it, 'next') and
        callable(it.__iter__) and
        it.__iter__() is it
    ):
        return True
    else:
        return False
        
def generator():
    yield 1
    print("generator 1")
    yield 2
    print("generator 2")
    yield 3
    print("generator 3")
    
g = generator()

'''
Arrays
http://www.i-programmer.info/programming/python/3942-arrays-in-python.html
http://www.i-programmer.info/programming/python/3942-arrays-in-python.html?start=1
http://stackoverflow.com/questions/27760831/assigning-values-to-an-array-with-for-loop-python
'''

def crive_primes(n):
    primes = [True] * n
    '''
        assign range array python
        http://stackoverflow.com/questions/11395057/python-set-list-range-to-a-specific-value
        Eratosthenes
        http://www.algorithmist.com/index.php/Prime_Sieve_of_Eratosthenes
        http://www.algolist.net/Algorithms/Number_theoretic/Sieve_of_Eratosthenes
    '''
    primes[0:1] = [False, False] # [False] * 2 
    for i in range(2, n+1):
        if(primes[i]):
            yield i
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    #return primes

'''   
if(isIterator(g)):
    for i in g:
        print(i)
'''       
rs = crive_primes(100)
if(isIterator(rs)):
    for i in rs:
        print(i)

#print(iterator(generator()))
#print(iterator(fibonacci(10)))


if __name__ == '__main__':
    pass