'''
Created on 7 de ago de 2016

@author: C.Lucas
'''
'''
https://docs.python.org/3/library/functions.html#map
'''

from sys import stdin


def runTestMapFunction():
    iterator = map(int, stdin.readline().split(' '))
    for i in iterator:
        print(i)


if __name__ == '__main__':
    pass