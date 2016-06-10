'''
Created on 6 de jun de 2016

@author: C.Lucas

https://www.urionlinejudge.com.br/judge/pt/problems/view/1398

Fatoracao em primos
https://en.wikipedia.org/wiki/Fermat_primality_test
http://stackoverflow.com/questions/12756335/fast-prime-factorization-algorithm
https://en.wikipedia.org/wiki/Primality_test

Number Theory - 1
https://www.hackerearth.com/notes/number-theory-1/
'''
from sys import stdin

def run(line):
    return None

def readEOF(fmt = None):
    while True:
        try:
            if fmt == None:
                line = stdin.readline()
            else:
                line = stdin.readline().split(fmt)
            while True:
                ch = stdin.read()
                if ch == '#':
                    break
                line += ch
        except:
            pass
        
readEOF()
if __name__ == '__main__':
    pass