'''
Created on May 23, 2016

@author: christoffer
'''

def expF(b, e):
    if(e == 1):
        return b
    elif(e < 0):
        b = 1/float(b)
        e = -e
    if(b%2==1):
        return b * expF(b, e-1)
    else:
        rs = expF(b, e/2)
        return rs * rs

def expFF(b, e):
    rs = 1
    if(e < 0):
        e = -e
        b = 1/float(b)
    elif(e == 1):
        return b
    elif(e == 0):
        return 1
    while e > 1:
        if e % 2 == 1:
            rs *= b
        e /= 2
        b *= b 
    return rs * b

def expFFF(b, e):
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

print(expF(3, 11))
print(expFF(3, 11))
print(expFFF(3, 11))


if __name__ == '__main__':
    pass