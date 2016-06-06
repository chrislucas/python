'''
Created on 28 de mai de 2016

@author: C.Lucas
DONE
'''

def factorial(n, acc):
    if(n < 2):
        return acc
    else:
        return factorial(n-1, acc*n)

from sys import stdin, stdout

def S():
    n = int(stdin.readline())
    stdout.write("%d" % ( factorial(n, 1) ) )

S()

if __name__ == '__main__':
    pass