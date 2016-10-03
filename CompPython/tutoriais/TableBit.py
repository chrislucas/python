'''
Created on Jun 3, 2016

@author: christoffer
'''
from math import log, log10
from sys import stdout


def tableTruth(n):
    for i in range(0,1<<n):
        for j in range(n-1, -1, -1): # ou range(0, n)
            stdout.write("%d" % (1 if (i & 1<<j) > 0 else 0))
        stdout.write("\n")  

def table(n):
    i = 0
    while i < (1<<n):
        #bit = [(0 if (1<<j & i) == 0 else 1) for j in range(0, n)]
        '''
        for j in range(n-1, -1, -1):
            stdout.write("%d" % (0 if (1<<j & i) == 0 else 1))
        stdout.write("\n")
        '''
        bit = [(0 if (1<<j & i) == 0 else 1) for j in range(n-1, -1, -1)]   
        print(bit)
        i+=1

#table(6)
#tableTruth(3)

'''
https://en.wikipedia.org/wiki/Bitwise_operation#AND
'''
def numbersOfBits(n):
    # famosa troca de bases para efeutar log n base 2
    return int( log10(n) /log10(2) ) + 1

def opNot(number):
    acc = 0
    for n in range(0, numbersOfBits(number)) :
        acc = acc + (2 ** n) * (((number // (2 ** n)) % 2 + 1) % 2)
    return acc

print(opNot(100))
print(~100)

if __name__ == '__main__':
    pass