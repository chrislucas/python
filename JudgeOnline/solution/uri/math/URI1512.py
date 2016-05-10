'''
Created on May 4, 2016

@author: christoffer
'''
from operator import mod
'''
Usando o principio da inclusao exclusao
dado um numero NUM contar quantos deles sao multiplos de A e B

Segundo o principio da inclusao-exclusao temos a seguinte formar

somatorio (A uniao B) = somatorio(A) + somatorio(B) - (somatorio (A interseccao B))

Por sua vez

somatorio (A interseccao B) = somatorio(A) + somatorio(B) - (somatorio (A UNIAO B))

'''
#from math import floor
from sys import stdin, stdout

def inc_exc(num, A, B):
    '''
    quantos numeros entre 1 e NUM
    sao divisiveis por A = piso[num/A]
    e por B = piso[num/B]
    '''
    return (num/A) + (num/B) - (num / lcm(A, B))


def lcm(a, b):
    return (a * b) / gdc(a, b)

def gdc(a, b):
    while (a % b) > 0:
        m = a % b
        a = b
        b = m
    return b
     
def readInts(fmt):
    return [int(e) for e in stdin.readline().split(fmt)]

def write(fmt, text):
    stdout.write(fmt % text)

def reader():
    Flag = True
    while Flag:
        num, A, B = readInts(" ")
        if(num == 0 and A == 0 and B == 0):
            break
        write("%d\n", inc_exc(num, A, B))
        
#write("%d", gdc(54, 4))
reader()
#print(inc_exc(1000000, 28, 32))

if __name__ == '__main__':
    pass