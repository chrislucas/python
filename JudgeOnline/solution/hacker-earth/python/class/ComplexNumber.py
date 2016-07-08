'''
Created on 5 de jul de 2016

@author: C.Lucas
https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers

http://xahlee.info/perl-python/complex_numbers.html
https://docs.python.org/3/c-api/complex.html
http://mundoeducacao.bol.uol.com.br/matematica/potencia-i.htm
'''
from sys import stdin, stdout

'''
http://xahlee.info/perl-python/complex_numbers.html
'''


'''
http://pessoal.sercomtel.com.br/matematica/medio/ncomplex/ncomplex.htm
'''

'''
http://mundoeducacao.bol.uol.com.br/matematica/divisao-numeros-complexos.htm
'''

def mulComplexNumbers(rA, iA, rB, iB):
    A = complex(rA, iA)
    B = complex(rB, iB)
    return A.__mul__(B)

def sumComplexNumbers(rA, iA, rB, iB):
    A = complex(rA, iA)
    B = complex(rB, iB)
    return A.__add__(B)

def minusComplexNumbers(rA, iA, rB, iB):
    A = complex(rA, iA)
    B = complex(rB, iB)
    return A.__sub__(B)

def divComplexNumbers(rA, iA, rB, iB):
    '''
    z.w = (a+bi).(c+di) = (ac-bd) + (ad+bc)i
    complex((rA*rB-iA*iB), (rA*iB+iA*rB))
    
    z/w = (z * conj(w)) / (w*conj(w))
    conjugado de w (a+bi) eh (a+(-b)i)
    
    ans = "{0}+{1}i".format( _sReal , _sImag)
    '''

    #A = complex(rA, iA)
    #B = complex(rB, iB)
    #cB = complex(rB, -iB)
    #cB = B.conjugate()
    
    num = mulComplexNumbers(rA, iA, rB, -iB) #A.__mul__(cB)
    dem = mulComplexNumbers(rB, iB, rB, -iB) #B.__mul__(cB)
    
    if num.imag == 0 and dem.imag == 0:
        return num.real / dem.real
    elif dem.imag == 0:
        rs = complex(num.real/dem.real, num.imag/dem.real)
        return rs
    else:
        rs = complex(num.real/dem.real, num.imag/dem.imag)
        return rs

'''
http://www.profcardy.com/cardicas/modulo-numero-complexo.php
'''
def modComplexNumber(rA, iA):
    a = complex(rA, iA)
    return None
    
def runTests():
    #cca = complex(2,1)
    #ccb = complex(5,6)
    #print(cca)
    #print(cca.real, cca.imag)
    #print(ccb.real, ccb.imag)
    '''
    print(cca.__add__(ccb))
    print(cca.__sub__(ccb))
    print(cca.__mul__(ccb))
    '''
    divComplexNumbers(2, 3, 1, 2)
    divComplexNumbers(2, 1, 5, 6)
    divComplexNumbers(2, 3, 4, -6)
    divComplexNumbers(2, 5, 1, -2)
    divComplexNumbers(4, 3, 2, 6)

'''
http://www.profcardy.com/cardicas/modulo-numero-complexo.php
http://www.profcardy.com/cardicas/modulo-numero-complexo.php
'''

def modComplexNumbers():
    return None

def run():
    _realA, _imagA = [int(x) for x in stdin.readline().split(" ")]
    _realB, _imagB = [int(x) for x in stdin.readline().split(" ")]
    ans = sumComplexNumbers(_realA, _imagA, _realB, _imagB)
    # https://pyformat.info/
    #https://docs.python.org/3.1/library/string.html
    msg = '{:.2f}{:s}{:.2f}i\n'.format(ans.real, '' if ans.imag < 0 else '+', ans.imag)
    
    ans = minusComplexNumbers(_realA, _imagA, _realB, _imagB)
    msg += '{:.2f}{:s}{:.2f}i\n'.format(ans.real, '' if ans.imag < 0 else '+', ans.imag)
    
    ans = mulComplexNumbers(_realA, _imagA, _realB, _imagB)
    msg += '{:.2f}{:s}{:.2f}i\n'.format(ans.real, '' if ans.imag < 0 else '+', ans.imag)
    
    ans = divComplexNumbers(_realA, _imagA, _realB, _imagB)
    msg += '{:.2f}{:s}{:.2f}i\n'.format(ans.real, '' if ans.imag < 0 else '+', ans.imag)
    
    stdout.write(msg)
    
run()

if __name__ == '__main__':
    pass