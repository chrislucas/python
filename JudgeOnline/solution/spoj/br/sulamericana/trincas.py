'''
Created on 25 de nov de 2016

@author: C.Lucas
'''

if __name__ == '__main__':
    pass

# http://br.spoj.com/problems/TRINCAS/
# http://br.spoj.com/problems/DTT/
# https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1931
# DP

'''
trios pitagoricos
https://pt.wikipedia.org/wiki/Problema_booleano_dos_trios_pitag%C3%B3ricos
'''

from sys import stdin

def isTriangle(a, b, c):
    if( (a + b > c and abs(a - b) < c) 
        and (b + c > a and abs(b - c) < a)
        and (a + c > b and abs(a - c) < b)):
        if (a != b and a != c and b == c 
            or (b != a and b != c and a == c)
            or (c != a and b != c and a == b) ):
            return 1    # isoceles
        elif(a == b and b == c):
            return 2    # equilatero
        else:
            return 3    # escaleno
    else:
        return -1


def run():
    num = int(stdin.readline())
    cartas = [int(x) for x in stdin.readline().split(" ")]