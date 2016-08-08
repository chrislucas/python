'''
Created on 7 de ago de 2016

@author: C.Lucas
'''
from sys import stdin

'''
https://docs.python.org/3/library/functions.html#map
'''

def runTestMapFunction():
    iterator = map(int, stdin.readline().split(' '))
    for i in iterator:
        print(i)


if __name__ == '__main__':
    pass