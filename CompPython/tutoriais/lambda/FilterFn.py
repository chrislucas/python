'''
Created on 6 de dez de 2016

@author: C.Lucas

http://www.secnetix.de/olli/Python/lambda_functions.hawk
http://www.python-course.eu/python3_lambda.php
'''

# https://docs.python.org/3/library/functions.html#filter
# filter(function, iterator)

def even(x):
    return x & 1 == 0

def odd(x):
    return not even(x)

def filterEvenNumbers(numbers):
    if(hasattr(numbers, '__iter__')):
        return list(filter(even, numbers))
    return list()

def filterOddNumbers(numbers):
    if(hasattr(numbers, '__iter__')):
        return list(filter(odd, numbers))
    return list()

print(filterEvenNumbers(range(1,9)))
print(filterOddNumbers(range(1,9)))

if __name__ == '__main__':
    pass