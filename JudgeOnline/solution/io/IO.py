'''
Created on Apr 27, 2016

@author: christoffer
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
    def writefmt(self, data, fmt = None):
        if(fmt is None):
            stdout.write(data)
        else:
            stdout.write(fmt % (data))   
    
    def writestr(self, data, fmt = None):
        if(fmt is None):
            stdout.write(data)
        else:
            stdout.write(fmt % str(data))  
    
    def write(self, data):
        stdout.write("%s" % str(data))
    
    def writeArgs(self, fmt, *args):
        stdout.write(fmt % args)
    
    # http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    def writeDouble(self, _str, fmt):
        stdout.write(fmt % float(str(_str)))
        
    def readFloatList(self, fmt):
        return [float(e) for e in stdin.readline().split(fmt)]
    
    def readIntList(self, fmt):
        return [int(e) for e in stdin.readline().split(fmt)]
    
def s():
    while True:
        try:
            n = CompIO.readFloat()
            CompIO().write(n)
        except:
            break

s()

'''
formatando a saida
https://docs.python.org/3/tutorial/inputoutput.html
'''

#https://docs.python.org/3/library/functions.html#input

#inn = input('---> ')
#CompIO().write(inn)


if __name__ == '__main__':
    pass