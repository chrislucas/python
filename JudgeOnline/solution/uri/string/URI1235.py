'''
Created on 19 de mai de 2016

@author: C.Lucas

DONE
https://www.urionlinejudge.com.br/judge/pt/problems/view/1235

'''

from sys import stdin, stdout

class CompIO():
    def __init__(self):
        pass
    
    def getMapInt(self, fmt):
        return map(int, stdin.readline().splt(fmt))
    
    def readAndSplit(self, fmt):
        return stdin.readline().split(fmt)
    
    def readStringList(self, fmt):
        n = stdin.readline().split(fmt)
        return [e for e in n]
    
    def readInt(self):
        return int(stdin.readline())
    
    def readFloat(self):
        return float(stdin.readline())
    
    def readLine(self):
        return stdin.readline()
    
    # python nao suporta overload de metodos
    # mas suporta default values, como no parametro fmt
    # abaixo
    def writeString(self, _str, fmt = None):
        if(fmt is None):
            stdout.write(_str)
        else:
            stdout.write(fmt % str(_str))   
    
    def write(self, _str):
        stdout.write("%s" % str(_str))
    
    def writeArgs(self, fmt, *args):
        stdout.write(fmt % args)
    
    # http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    def writeDouble(self, _str, fmt):
        stdout.write(fmt % float(str(_str)))
        
    def readFloatList(self, fmt):
        return [float(e) for e in stdin.readline().split(fmt)]
    
    def readIntList(self, fmt):
        return [int(e) for e in stdin.readline().split(fmt)]

io = CompIO()

def process(_str):
    _len = len(_str)-1
    _mid = _len/2-1 if _len % 2 == 0 else _len/2
    _mid = int(_mid)
    _ans = [None] * _len
    count = 0
    for i in range(0, _len):
        if(i <= _mid):
            idx = _mid - i
        else:
            idx = (_len-1) - count
            count += 1
        _ans[idx] = _str[i]
    
    io.writeString("".join(_ans), "%s\n")
    
def solution():
    n = io.readInt()
    i = 0
    while i < n:
        _str = io.readLine()
        process(_str)
        i += 1

solution()

if __name__ == '__main__':
    pass