'''
Created on 8 de ago de 2016

@author: C.Lucas

https://docs.python.org/2/library/collections.html
'''
from sys import stdin, stdout
from collections import Counter

# class collections.Counter([iterable-or-mapping])
def usingCounterClass():
    _dict = Counter({'a' : 1 ,'b' : 2, 'c': 3})
    print(_dict)
    # <itertools.chain object at 0x028B3890>
    #print(_dict.elements())
    for it  in _dict.elements():
        stdout.write("%s " % (it))
        
def run():
    cases = int(stdin.readline())
    cards = list(map(int, stdin.readline().split(' ')))
    '''
    counter is a dict subclass for counter hashtables objects
    interessante que Counter ordena o mapa de forma decrescente
    a partir da chave com mais elementos no Map
    '''
    count = Counter(cards)
    print(count)

def run2():
    cases = int(stdin.readline())
    cards = list(map(int, stdin.readline().split(' ')))
    cards.sort()
#run()
usingCounterClass()
if __name__ == '__main__':
    pass