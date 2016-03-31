'''
Created on Mar 30, 2016

@author: christoffer
'''
from math import sqrt, modf
from sys import stdout

#https://www.easycalculation.com/statistics/standard-deviation.php
#https://www.easycalculation.com/statistics/learn-standard-deviation.php

def sepIntFromDec(num, dec):
    arr = []
    dec = 10 ** dec
    arr.insert(0, int(num * dec / dec))
    arr.insert(1, int(num * dec % dec))
    return arr

def _int(n):
    try:
        return int(n)
    except ValueError:
        pass

def mean(numbers):
    s = 0.0
    for e in numbers:
        s+= _int(e)
    return s / len(numbers)

def populatitionStdDev(numbers, mean):
    N = len(numbers)
    s = 0.0
    for i in numbers:
        s += ((i - mean) ** 2)
    return sqrt(s/(N))

def standardDeviation(numbers, mean):
    N = len(numbers)
    s = 0.0
    for i in numbers:
        s += ((i - mean) ** 2)
    return sqrt(s/(N-1))

def variance(numbers, mean):
    return standardDeviation(numbers, mean) ** 2

def printDouble(fmt, number):
    stdout.write(fmt % number)

#print(sepIntFromDec(10.89, 2))
'''
n = [5,10,15,20,25]#[1,2,3]
m = mean(n)
printDouble("%f\n", m)
printDouble("%f\n", standardDeviation(n, m))
printDouble("%f\n", variance(n, m))
printDouble("%f\n", populatitionStdDev(n, m))
print(sepIntFromDec(populatitionStdDev(n, m), 2))
'''
numbers = [1,2,3]
m = mean(numbers)
d = populatitionStdDev(numbers, m)

def almostEquals(a, b):
    eps = 10E-1
    print(modf(a-b))
    return True if ( modf(a-b) <= eps )   else False

def floatRange(a, b, step):
    L = []
    s = 1.0
    for i in range(a, b):
        s += 0.1
        L.insert(i, s)
    return L 
       
        
        
def solution(numbers):
    List = floatRange(0, 100, 1.0)
    for k, i in List :
        numbers.insert(3, i)
        m = mean(numbers)
        x = populatitionStdDev(numbers, m)
        stdout.write( "%f %.2f %.2f" % (i, d, x) )
        if(almostEquals(d, x)):
            return [i, x]
        numbers.remove(i)
        
print(solution(numbers))    
    
if __name__ == '__main__':
    pass