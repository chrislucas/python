'''
Created on 28 de dez de 2015

@author: C.Lucas
'''
#from cmath import log
from math import log2
from builtins import print

x = 0
y = 0
limit = 1<<3
# tabela de la verdad :)
while x < limit:
    for y in range(int(log2(limit))-1, -1, -1):
        msg = '1' if x & (1 << y) > 0 else '0'
        print (msg , sep=' ', end='')
    print("")
    x+=1

'''
links sobre string interpolation e operacoes com strings
http://stackoverflow.com/questions/13945749/string-formatting-in-python-3
https://docs.python.org/3.1/library/string.html
''' 
#interpolacao
sfmt = "tamanho de \'{0}\', {1}".format('uma frase qualquer', len('uma frase qualquer')) 
print(sfmt)
#interpolacao
sfmt = "%d %.2f" % (12, 3.14)
print(sfmt)

if __name__ == '__main__':
    pass