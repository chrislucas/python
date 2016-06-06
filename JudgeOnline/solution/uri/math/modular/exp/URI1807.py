'''
Created on 6 de jun de 2016

@author: C.Lucas
DONE
'''
from math import log10
from sys import stdin, stdout

class CompIO():
    def __init__(self):
        pass

    def readInt(self):
        return int(stdin.readline())

    # python nao suporta overload de metodos
    # mas suporta default values, como no parametro fmt
    # abaixo
    def writefmt(self, data, fmt = None):
        if(fmt is None):
            stdout.write(data)
        else:
            stdout.write(fmt % (data))   
    
    def write(self, _str):
        stdout.write("%s" % str(_str))
    
    def writeArgs(self, fmt, *args):
        stdout.write(fmt % args)
    
    # http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    def writeDouble(self, _str, fmt):
        stdout.write(fmt % float(str(_str)))
        

def log(lg, base):
    return log10(lg) / log10(base)

def decToBin(num):
    sz = int(log(num, 2)) + 1
    _bin = [None] * sz
    for i in range(sz-1, -1, -1):
        _bin [i] = True if (num & 1) == 1 else False
        num >>= 1
    return _bin

def modularExpLF(base, e, _mod):
    if(e == 0):
        return 1
    elif(e < 0):
        e = -e
        base = 1/base
    elif(e == 1):
        return base
        
    _bin = decToBin(e)
    ans = 1
    for bit in (_bin):
        ans = (ans * ans) % _mod
        if(bit):
            ans = (ans * base) % _mod
    return ans;


#print(modularExpLF(3, 2, (1<<31)-1))

def sol():
    io  = CompIO()
    n   = io.readInt()
    io.writefmt(modularExpLF(3, n, (1<<31)-1), "%d\n")

sol()

if __name__ == '__main__':
    pass