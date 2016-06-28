'''
Created on 6 de jun de 2016

@author: C.Lucas
https://www.urionlinejudge.com.br/judge/pt/problems/view/1279

http://pessoal.sercomtel.com.br/matematica/fundam/naturais/divisibilidade.htm#m103b11
http://www.somatematica.com.br/fundam/critdiv.php
'''
from math import log10
from sys import stdout, stdin


def isLeap(year):
    if( (year % 4 == 0) and (year % 100 > 0 or year % 400 == 0) ):
        return True
    else:
        return False

def numDigits(num):
    return int(log10(num))
 
def divBy11(num):
    lf = 0
    ri = 0
    div = 10 ** ( numDigits(num) )
    flip = True
    while num >= 1:
        if(flip):
            lf += num // div
        else:
            ri += num // div
        num %= div
        div //= 10
        flip = not flip
    diff = (lf - ri) if (lf - ri) > 0 else -(lf - ri)
    return True if diff % 11 == 0 else False


def strDivBy3(_str):
    _sum = 0
    for d in _str:
        _sum += int(d)
    return _sum % 3 == 0

def strDivBy4(_str):
    # slicing string
    s = _str[-2:]
    num = int(s)
    return num % 4 == 0

def strDivBy5(_str):
    lastDigit = int(_str[-1:])
    return lastDigit == 0 or lastDigit == 5

def strDivBy15(_str):
    #n = int(_str)
    #return n % 3 == 0 and n % 5 == 0
    return strDivBy3(_str) and strDivBy5(_str)

def strDivBy100(_str):
    return int(_str[-2:]) == 0

def divBy100(num):
    return (num % 100) % 10 == 0

def strDivBy400(_str):
    return strDivBy100(_str) and strDivBy4(_str)

def strDivBy55(_str):
    return strDivBy11(_str) and strDivBy5(_str)

def strDivBy11(_str):
    lf = 0
    ri = 0
    flip = True
    for num in _str:
        if(flip):
            lf += int(num)
        else:
            ri += int(num)
        flip = not flip
    diff = (lf - ri) if (lf - ri) > 0 else -(lf - ri)
    return True if diff % 11 == 0 else False

def runTest():
    l = [121, 29458, 1353, 2543, 111, 1111, 87549, 439087]
    for num in l:
        stdout.write("%s %s\n" % (strDivBy11(str(num)), divBy11(num) ) )
    
#runTest()

print(strDivBy4("43143543534534534512"))
print(strDivBy100("4314354353453453451200"))

def run():
    while True:
        try:
            num = stdin.readline()
        except:
            break


if __name__ == '__main__':
    pass