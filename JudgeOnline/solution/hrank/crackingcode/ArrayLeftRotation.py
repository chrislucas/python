'''
Created on 19 de nov de 2016

@author: C.Lucas
'''

# https://www.hackerrank.com/challenges/ctci-array-left-rotation
# done

from sys import stdin, stdout

def _abs(a):
    return a if a >= 0 else -a

def array_left_rotation(_list, _size, shift):
    indexes = [None] * _size
    for idx in range(0, _size):
        indexes[(idx - shift + _size) % _size] = _list[idx]
    return indexes

def array_right_rotation(_list, _size, shift):
    indexes = [None] * _size
    for idx in range(0, _size):
        indexes[(idx + shift) % _size] = _list[idx]
    return indexes
    

def stdIn():
    return stdin.readline()

def solver():
    _size, _rotation = map(int, stdIn().split(' '))
    _list = list(map(int, stdIn().split(' ')))
    answer = array_left_rotation(_list, _size, _rotation);
    #stdout.write(answer)
    print(*answer, sep=" ")
    #answer = array_right_rotation(_list, _size, _rotation);
    #print(*answer, sep=" ")
    
    
solver()

if __name__ == '__main__':
    pass