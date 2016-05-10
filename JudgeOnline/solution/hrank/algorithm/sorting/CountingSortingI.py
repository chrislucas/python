'''
Created on May 10, 2016

@author: christoffer
'''
'''
https://www.hackerrank.com/challenges/countingsort1/forum
DONE
'''
from sys import stdin, stdout

class CompIO():
    
    def __init__(self):
        pass
    
    def readAndSplit(self, fmt):
        return stdin.readline().split(fmt)

    def readInt(self):
        return int(stdin.readline())
    
    def readFloat(self):
        return float(stdin.readline())
    
    # python nao suporta overload de metodos
    # mas suporta default values, como no parametro fmt
    # abaixo
    def writeString(self, _str, fmt = None):
        if(fmt is None):
            stdout.write(_str)
        else:
            stdout.write(fmt % str(_str))        
    
    # http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    def writeDouble(self, _str, fmt):
        stdout.write(fmt % float(str(_str)))
        
    def readFloatList(self, fmt):
        return [float(e) for e in stdin.readline().split(fmt)]
    
    def readIntList(self, fmt):
        return [int(e) for e in stdin.readline().split(fmt)]
    

def solution(_list, n):
    # inicializando um array com 0 (zeros) do tamanho do array
    # passado por parametro
    rs = [0] * 100
    i = 0
    while i < n:
        rs[ _list[i]  ] += 1
        i+=1
        
    for i in rs:
        io.writeString(i, "%s ")

io = CompIO();
n = io.readInt()
_list = io.readIntList(" ")
solution(_list, n)


if __name__ == '__main__':
    pass