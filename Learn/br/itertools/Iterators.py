'''
Created on 14 de jul de 2016

@author: C.Lucas
'''
from itertools import count, repeat


'''
https://docs.python.org/3.5/library/itertools.html
'''


# Infinite Iterators
def test_count(start, step, limit=10):
    #for x in count(10, 0.01):
        #print(x)
   
    while start < limit:
        start += step
        yield start

#print([x for x in test_count(10, 0.5, 20)])
    
def test_repeat(m, n):
    '''
    def repeat(object, times=None)
        if times is None:
            while True:
                yield object
        else
            for i in range(times)
                yield object
    '''
    s = repeat(m,n)
    print([x for x in s])

#test_repeat(10, 3)

def f(m, n):
    return m % n

def run_test_map(limit):
    #_map_object = map(lambda x : x**3, range(limit))
    #print("%s\n" % ([v for v in _map_object]))
    
    # dictonary comprehension
    #print( { k:v for k,v in {10:5,12:3}.items() })
    
    '''
    http://stackoverflow.com/questions/10834960/how-to-do-multiple-arguments-to-map-function-where-one-remains-the-same-in-pytho
    '''
    print( "%s\n" % ( [f(k,v) for k,v in {10:6,12:7}.items() ]) )
    print( "%s\n" % ( [i for i in repeat(2, 10) ] ) )
    print( "%s\n" % ( list(map(f, range(limit), repeat(2, limit))) ) )
    
    #for k in map(pow, range(limit), repeat(2)):
        #print(k)   

run_test_map(10)

# fim infinite Iterators
'''
http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
'''
def test_generators(times):
    '''
        Ponto interessante:
        Quando usamos iterables, armazenamos todos os elementos
        em memoria.
        Generators sao iterator mas podemos iterar sobre eles
        uma unica vez. Os valores de um iterator nao estao
        todos armazenados na memoria
    '''
    _generator = (x*x for x in range(times))
    print([i for i in _generator])
    # que fita
    print([i for i in _generator])

#test_generators(3)

'''
Keyword usado para que a funcao retorne um generator
'''
def test_yeld(times):
    for i in range(1, times+1):
        yield i*i
    for i in range(1, times+1):
        i*i

def run_test_yield():
    _gen = test_yeld(10)    
    print([x for x in _gen])
    print([x for x in _gen])

#run_test_yield()    

# fim teste yield  
    
if __name__ == '__main__':
    pass