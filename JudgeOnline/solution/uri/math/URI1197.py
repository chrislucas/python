'''
Created on Mar 15, 2016

@author: christoffer

'''

from sys import stdin, stdout

def solution(v, t):
    return v * t * 2 

def reader():
    return stdin.readline()

def writer(data):
    stdout.write("%d\n" % (int(str(data))) )

while(True):
    try:
        _values = stdin.readline().split(" ")
        v = int(_values[0])
        t = int(_values[1])
        writer(solution(v, t))
    except:
        break

if __name__ == '__main__':
    pass