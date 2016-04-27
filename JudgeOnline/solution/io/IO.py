'''
Created on Apr 27, 2016

@author: christoffer
'''

from sys import stdin, stdout

class CompIO():
    
    def __init__(self):
        pass
    
    def readAndSplit(self, fmt):
        return stdin.readline().split(fmt)

    def readInt(self):
        return int(stdin.readline())
    
    def readFloar(self):
        return float(stdin.readline())
    
    def writeString(self, _str):
        stdout.write(_str)
    
    # http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    def writeDouble(self, _str, fmt):
        stdout.write(fmt % float(str(_str)))
        
    def readFloatList(self, fmt):
        return [float(e) for e in stdin.readline().split(fmt)]
    
def s():
    while True:
        try:
            n = CompIO.readFloar()
        except:
            break
        


if __name__ == '__main__':
    pass