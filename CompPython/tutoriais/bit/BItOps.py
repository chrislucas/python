'''
Created on 6 de dez de 2016

@author: C.Lucas
https://en.wikipedia.org/wiki/Two's_complement
'''

def rmsb(n):
    return n & (-n)

def fnLog(n, base):
    from math import log10
    return log10(n) / log10(base) 

def posRMSB(n):
    return int(fnLog(rmsb(n), 2))


def complement1(n):
    return ~n

'''
numeros negativos tem sua representacao binaria
usando complmento de 2
'''
def complement2(n):
    return complement1(n) + 1

#print(fnLog(100, 2))

print("{0} {1} {2}".format(complement2(5), ~5 + 1, ~(-5)))

print("{0} {1}\n".format(rmsb(127), posRMSB(127)))


#print([rmsb(x) for x in range(0, 2 << 12)])

if __name__ == '__main__':
    pass