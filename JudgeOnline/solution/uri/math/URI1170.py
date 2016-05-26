'''
Created on May 20, 2016

@author: christoffer
DONE
https://www.urionlinejudge.com.br/judge/pt/ranks/problem/1170/python3
'''

from sys import stdin, stdout
from math import log, ceil


cases = int(stdin.readline())

for i in range(0, cases):
    sup = int(float(stdin.readline()))
    stdout.write( "%d dias\n" % ceil(log(sup, 2)))

if __name__ == '__main__':
    pass