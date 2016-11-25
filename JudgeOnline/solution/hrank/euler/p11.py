'''
Created on 19 de nov de 2016

@author: C.Lucas
'''

'''
DONE
'''

if __name__ == '__main__':
    pass

# https://www.hackerrank.com/contests/projecteuler/challenges/euler011

from sys import stdin

def stdIn():
    return stdin.readline()

def analysingRight(matrix, i, j, n):
    ans = 1
    for x in range(j, n):
        val = matrix[i][0][x]
        if(val == 0):
            return 0
        ans *= val

    return ans

def analysingDown(matrix, i, j, n):
    ans = 1
    for x in range(i, n):
        val = matrix[x][0][j]
        if(val == 0):
            return 0
        ans *= val
    return ans


def analysingDiagonalLeft(matrix, i, j, n):
    ans = 1
    #for y in range(j, n-j-1, -1):
    while(i<n):
        val = matrix[i][0][j]
        if(val == 0):
            return 0
        ans *= val
        i += 1
        j -= 1
    return ans

def analysingDiagonalRight(matrix, i, j, n):
    ans = 1
    #for x in range(j, n):
    while(j<n):
        #val = matrix[x][0][x]
        val = matrix[i][0][j]
        if(val == 0):
            return 0
        ans *= val
        i += 1
        j += 1
    return ans

def run():
    _sz = 20 #20
    Matrix = [[]*_sz]*_sz
    for i in range(_sz):
        Matrix[i] = [[int(n) for n in stdIn().rstrip().split(" ")]]
    _max, n = 0, 4
    for i in range(_sz):
        for j in range(_sz):
            if(j <= _sz-n):
                _ans = analysingRight(Matrix, i, j, j+n)
                _max = _ans if _ans> _max else _max
            
            if(i <= _sz-n):
                _ans = analysingDown(Matrix, i, j, i+n)
                _max = _ans if _ans > _max else _max
                
            if(i <= _sz-n and j <= _sz-n):
                _ans = analysingDiagonalRight(Matrix, i, j, j+n)
                _max  = _ans if _ans > _max else _max
                
            if(i <= _sz-n and j >= n-1):
                _ans = analysingDiagonalLeft(Matrix, i, j, i+n)
                _max  = _ans if _ans > _max else _max
    return _max

print(run())