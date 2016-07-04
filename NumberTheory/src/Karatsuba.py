'''
Created on 3 de jul de 2016

@author: C.Lucas
'''
from math import ceil, floor

def fexp(b, e):
    rs = 1
    if(e < 0):
        e = -e
        b = 1/float(b)
    elif(e == 1):
        return b
    elif(e == 0):
        return 1
    while e > 1:
        if e & 1 == 1:
            rs *= b
        e >>= 1
        b *= b 
    return rs * b


'''
http://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/karatsuba.html
'''
def karatsuba_ofman(u, v, n):
    if(n <= 3):
        return u * v
    else:
        m = ceil(n/2)
        G = fexp(10, m)
        p = floor(u/G)
        q = u%G
        r = floor(v/G)
        s = v%G
        pr = karatsuba_ofman(p, r, m)
        qs = karatsuba_ofman(q, s, m)
        y = karatsuba_ofman(p+q, r+s, m+1)
        H = fexp(10, 2*m)
        I = fexp(10, m)
        x = pr * H + (y -pr - qs) * I + qs
        return x
print(fexp(10, 7))
print(karatsuba_ofman(6514202, 9898989, 7))
print(karatsuba_ofman(9999, 7777, 4))
print(karatsuba_ofman(9999, 7, 4))

if __name__ == '__main__':
    pass