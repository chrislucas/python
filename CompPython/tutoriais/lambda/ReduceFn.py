'''
Created on 6 de dez de 2016

@author: C.Lucas
http://stackoverflow.com/questions/13638898/how-to-use-filter-map-and-reduce-in-python-3
'''

from functools import reduce

def odd(x):
    return x & 1 == 1

def add(x, y):
    return x + y

def sumOfOddNumbers(numbers):
    if(hasattr(numbers, '__iter__')):
        return reduce(add, filter(odd, numbers))
    return 0

def sumOfRange(numbers):
    if(hasattr(numbers, '__iter__')):
        # reduce(lambda x, y: x+y, numbers)
        return reduce(add, numbers)
    return 0

print(sumOfOddNumbers(range(0,11)))
print(sumOfRange(range(0,11)))

if __name__ == '__main__':
    pass