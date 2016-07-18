'''
Created on 15 de jul de 2016

@author: C.Lucas
http://www.python-course.eu/python3_generators.php
'''
from sys import stdin, stdout
import itertools

def fib(n):
    a,b,count = 0, 1, 0
    while(count < n):
        yield a
        a = b - a
        b = a + b
        count += 1
        
def runFib():
    n = int(stdin.readline())
    numbers = fib(n)
    print([x for x in numbers])
    
    
def perm(_str):
    new_str = itertools.permutations(_str)
    out = list(new_str)
    return out

def powerset(_str):
    n = len(_str)
    if(n == 0):
        yield []
        return None
    for i in range(0, 1<<n):
        _set = []
        #for j in range(n-1, -1, -1):
        for j in range(0, n):
            x = 0 if (i & 1<<j) == 0 else 1
            #stdout.write("%d" %(x))
            if(x == 1):
                #stdout.write("%s" %(_str[j]))
                _set.append(_str[j])
        #stdout.write('\n')
        yield _set
        
print(perm('asd'))
print(list(powerset('asd')))
print(list(powerset('')))

if __name__ == '__main__':
    pass