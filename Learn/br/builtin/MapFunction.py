'''
Created on 17 de jul de 2016

@author: C.Lucas
https://docs.python.org/3/library/functions.html#map
'''
from builtins import map

def f(n):
    return n ** 3
# recebe uma funcao e um iterable como argumento
# aplica a funcao em cada item do iterable
# retorna um iterator
#print(list(map(f, [1,2,3])))

def g(m, n):
    return m*n

print(list(map(g, [1,2,3], range(0,3))))

if __name__ == '__main__':
    pass