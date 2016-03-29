'''
Created on Mar 18, 2016

@author: christoffer
'''

# https://www.hackerrank.com/challenges/and-product

# format string https://pyformat.info/

from sys import stdin, stdout

def solution(a, b):
    s = int(a) #+ 1 if int(a) & 1 == 0 else int(a)
    for i in range(a, b):
        #stdout.write("%d %d\n" % ( int(s), int(i+1) ) )
        s = s & int(i)
    return s

def bit(a, b):
    a = int(a)
    b = int(b)
    x = 0
    while( (a|x) < b ):
        x = (x << 1) | 1
    return a & ~x

def read():
    return stdin.readline()

def readSplit(fmt):
    return stdin.readline().split(fmt)

def printInt(fmt, data):
    stdout.write(fmt % int(str(data)) )
      
def printString(fmt, data):
    stdout.write(fmt % str(data) )

cases   = int(read())

while(cases > 0):
    values  = readSplit(" ")
    a = int(values[0])
    b = int(values[1])
    printInt("%d\n", bit(a, b))
    cases-=1 



if __name__ == '__main__':
    pass