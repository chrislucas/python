'''
Created on May 5, 2016

@author: christoffer
'''
from sys import stdout
from math import sqrt
from inspect import isgenerator
from solution.uri.test.Generators import isIterator


'''
Aprendendo a usar o Yield
https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
https://docs.python.org/3/whatsnew/3.3.html

https://diofeher.wordpress.com/2011/04/12/explicando-iterables-generators-yield-no-python/
http://www.python-course.eu/python3_generators.php

Co-rotinas e subrotinas
chamemos as funcoes padrao de subrotinas por hora
O funcionamento padrao de uma funcao em python, como na maioria das linguagens, acontece
linha a linha da funcao ateh que a ultima linha que podera ter uma clausula return ou nao
ter essa linha, onde no python ha quando nao tem a clausula return e colocado de forma implicica
return None. Apos o funcionamento da funcao, todas as variaveis locais sao descartadas.

As vezes, surge a necessidade de se ter uma funcao que retorne muitos valores.
OBS Yield -> Producao

A palavra chave 'yield' no python permite modificar a forma que uma funcao retorna apos
a sua execucao, possibilitando o retorno de muitos valores. Essa mudancao ocorre pos do
ponto de vista do funcionamento normal de uma funcao, quando ocorre o fim de execucao dela
o controle volta para o ponto onde a funcao foi chamada. O uso do yield implica que havera uma
transferencia de controle para o chamador, de forma temporaria, e que a funcao espera ter o controle
de volta ate terminar a execucao.

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
    
'''
Funcoes que utilzando yield sao chamadas de generator.

Fora do contexto do python, generator pode ser chamados de Co-routines
'''      
def generator():
    yield 1
    print("generator 1")
    yield 2
    print("generator 2")
    yield 3
    print("generator 3")

def test_generator():   
    g = generator()
    for i in g:
        print(i)
        
#test_generator()


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

def is_prime_sqrt(n):
    if(n<2 or (n%2==0 and n!=2) or (n%3==0 and n!=3) or (n%5==0 and n!=5)):
        return False
    for i in range(7, int(sqrt(n))+1):
        if(n%i == 0):
            return False
    return True

def make_list_prines(n):
    return (element for element in range(1, n+1) if is_prime_sqrt(element))

def print_list():
    g = make_list_prines(100)
    if(isIterator(g)):
        for i in g:
            print(i)


'''   
if(isIterator(g)):
    for i in g:
        print(i)
'''       
'''
rs = crive_primes(100)
if(isIterator(rs)):
    for i in rs:
        print(i)
'''
#print(is_prime_sqrt(237))

#print(iterator(generator()))
#print(iterator(fibonacci(10)))


if __name__ == '__main__':
    pass