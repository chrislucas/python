'''
Created on May 5, 2016

@author: christoffer
'''
from sys import stdout

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
        
        
def generator():
    yield 1
    print("Teste")
    yield 2
    yield 3
    
 
g = generator()
g.next()


#print(iterator(generator()))
#print(iterator(fibonacci(10)))


if __name__ == '__main__':
    pass