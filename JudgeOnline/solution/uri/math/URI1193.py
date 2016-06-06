'''
Created on May 20, 2016

@author: christoffer
'''
from sys import stdout

hexadecimal = {
     'a': 10
    ,'b': 11
    ,'c': 12
    ,'e': 13
    ,'e': 14
    ,'f': 15
}

def fastExponential(b, e):
    return None

def expSquaringRecursive(b, e, acc = 1):
    if(e == 0):
        return acc
    elif(e < 0):
        return  expSquaringRecursive(1/float(b), -e, acc)
    elif(e == 1):
        return b * acc
    elif( e % 2 == 0):
        return expSquaringRecursive(b*b, e/2, acc)
    else:
        return expSquaringRecursive(b*b, (e-1)/2, b*acc)

def expSquaringIterative(b, e, acc = 1):
    if e == 0:
        return acc
    elif e < 0:
        b = 1/float(b)
        e = -e
    elif e == 1:
        return acc * b
    while e > 1:
        if e % 2 == 0:
            e //= 2
        else:
            e = (e-1)//2
            acc *= b
        b *= b
    return b * acc

def binToHex(n):
    ans = n
    # im da funcao
    return ans

def binToDex(n):
    ans = 0
    e = len(n) - 1
    for i in range(0, len(n)):
        val = int(n[i])
        ans += expSquaringIterative(2, e-i) * val 
    return ans

def decToBin(n):
    ans = n

def decToHex(n):
    ans = n

def hexToBin(n):
    ans = n    

def hexToDec(n):
    ans = 0
    e = len(n) - 1
    for i in range(0, len(n)):
        val = n[i]
        
        '''
           metodo  has_key em dicionario no python 3 foi retirado
           use o in
        '''
        val = int(hexadecimal[val]) if val in hexadecimal else int(val)
        ans += val * expSquaringIterative(16, e - i) 
    return ans
    


def solution(n, base):   
    return None

print(expSquaringIterative(3, -3))
print(expSquaringRecursive(3, -3))


stdout.write("%d\n" % (hexToDec('8f')))
stdout.write("%d\n" %  (binToDex('1001')))
    
if __name__ == '__main__':
    pass