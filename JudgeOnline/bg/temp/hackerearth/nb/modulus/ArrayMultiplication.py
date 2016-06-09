'''
Created on Jun 9, 2016

@author: christoffer
https://www.hackerearth.com/practice/math-1/number-theory-1/modulus-arithmetic-1/tutorial/
DONE
'''
from sys import stdout, stdin

def solutionOne(array):
    acc = 1
    for num in array:
        acc = ((acc % 1000000007) * (num % 1000000007)) % 1000000007
    stdout.write("%d\n" % (acc))

def run():
    s       = int(stdin.readline())
    array   = [None] * s
    array   = [int(x) for x in stdin.readline().split(" ")]
    solutionOne(array)

run()

if __name__ == '__main__':
    pass