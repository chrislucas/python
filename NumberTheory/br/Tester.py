'''
Created on 29 de jun de 2016

@author: chrislucas
'''
from math import log10

def runTest():
    n = 100
    print(n ** (1/2)) # A
    print(10 ** n) # B
    print(n ** (1.5)) # C
    print(2 ** (log10(n) ** 1/2)) # D
    print(n ** (5/3)) # E
    
runTest()



if __name__ == '__main__':
    pass