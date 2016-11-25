'''
Created on 25 de nov de 2016

@author: C.Lucas
'''

if __name__ == '__main__':
    pass

'''
http://blog.hackerearth.com/prerequisites-linear-algebra-machine-learning
'''

import numpy as np
from numpy import abs, array, eye

def test_numpy_abs():
    print(abs([-1.2, 1.2]))

def test_numpy_array():
    matrix = array([[1,2,3],[3,2,1]])
    print(*matrix)
    print(matrix.shape)
    
def identity_matrix(n):
    print(eye(n))
    

def add_matrix():
    a = array([ [1,2,3],[3,2,1] ])
    b = array([ [1,2,3],[3,2,1] ])
    return np.add(a, b)

#print(add_matrix())
'''
http://cs231n.github.io/python-numpy-tutorial/
'''

print(np.transpose(add_matrix()))
print(np.ones((1, 2, 3)))
#print(np.arange(4).reshape((2,2)))