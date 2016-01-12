'''
Created on Jan 12, 2016

@author: christoffer
'''
from cmath import sqrt

'''
Python supports a concept called 'list comprehension'. It allow to write lists
in a very natural, easy way, like a mathematician is used to do.
'''
# S {x^2  : x in (0..9) }
S = [x ** 2 for x in range(10)]
#print(type(S))
#print (S)

# V {1, 2, 4, 8, ...  n^2}
V = [1 << x for x in range(10)]
#print (V)

# M {x | x in S and x even}
M = [x for x in S if x % 2 == 0]
#print(M)

def quad(limit):
    q = [j for i in range(2, limit+1) for j in range(i*i, (1<<limit)+1, i) ]
    return set(q)

def crive(n):
    numbers = [True] * n
    numbers[0] = False
    numbers[1] = False
    for i in range(2, int(n+1 ** 1/2)):
        if numbers[i] :
            j = i*i
            while j <= n:
                numbers.insert(j, False)
                j += i      
                
    
    return numbers
    
#print(type ([True] * 4) )
print(crive(80))
print(quad(5))

if __name__ == '__main__':
    pass