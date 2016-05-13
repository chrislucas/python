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
    
    def write(self, _str):
        stdout.write("%s" % str(_str))
    
    # http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    def writeDouble(self, _str, fmt):
        stdout.write(fmt % float(str(_str)))
        
    def readFloatList(self, fmt):
        return [float(e) for e in stdin.readline().split(fmt)]
    
def s():
    while True:
        try:
            n = CompIO.readFloar()
            CompIO().write(n)
        except:
            break

'''
formatando a saida
https://docs.python.org/3/tutorial/inputoutput.html
'''

#https://docs.python.org/3/library/functions.html#input

#inn = input('---> ')
#CompIO().write(inn)


if __name__ == '__main__':
    pass