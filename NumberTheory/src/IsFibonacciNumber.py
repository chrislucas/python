'''
Created on 28 de jul de 2016

@author: C.Lucas

Problem
https://www.hackerrank.com/challenges/is-fibo
DONE
'''
from sys import stdin, stdout
from math import sqrt

def isPerfectSquare(b):
    s = int(sqrt(b))
    return s*s == b

def isFibo(num):
    a = ( 5 * num*num + 4 )
    b = ( 5 * num*num - 4 )
    return isPerfectSquare(a) or isPerfectSquare(b)

def run():
    n = int(stdin.readline())
    while n>0:
        o = int(stdin.readline())
        stdout.write("%s\n" %('IsFibo' if isFibo(o) else 'IsNotFibo'))
        n -= 1

run()

if __name__ == '__main__':
    pass