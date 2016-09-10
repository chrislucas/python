'''
Created on 7 de set de 2016

@author: chrislucas

https://www.hackerrank.com/challenges/sherlock-and-gcd
'''

from sys import stdout

def gdc(a, b):
    while (a % b != 0):
        c = a % b
        a = b
        b = c
    return b

def gdcList(numbers):
    if(len(numbers) > 0):
        a = numbers[0]
        for b in range(1, len(numbers)):
            a = gdc(a, numbers[b])
    return a


def subset(_set):
    sizeSet = len(_set)
    for i in range(0, 1<<sizeSet):
        for j in range(0, sizeSet):
        #for j in range(sizeSet-1, -1, -1):
            if (( i&(1<<j) ) > 0):
                stdout.write("%d" % ( _set[j] ) )
            #stdout.write("%s" % ( '1' if ( i&(1<<j) ) > 0 else '0' ) )
        stdout.write("\n")
subset([1,2,3])

#print(gdc(54, 14))
#print(gdcList([54, 14]))





if __name__ == '__main__':
    pass