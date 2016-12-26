'''
Created on 25 de dez de 2016

@author: C.Lucas
'''
from builtins import round

if __name__ == '__main__':
    pass
'''
a)
C(4,3) = 4
C(4,4) = 1
https://www.hackerrank.com/challenges/binomial-distribution-1
'''

A = 4 * ( (4/5) ** 3) * ( (1/5) ** 1)
B = 1 * ( (4/5) ** 4) * ( (1/5) ** 0)
# {0:.2f} format string para float com casas decunaus
print( "{0} {1}".format(round(A+B, 3), A+B) )

'''
b
C(4,1) = 4
C(4,0) = 1
'''

A = 4 * ( (4/5) ** 1) * ( (1/5) ** 3)
B = 1 * ( (4/5) ** 0) * ( (1/5) ** 4)
print( "{0} {1}".format(round(A+B, 3), A+B) )