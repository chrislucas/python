'''
Created on 29 de mai de 2016

@author: C.Lucas
'''
import functools
import random


'''
Python supports the creation of anonymous functions
at runtime, using a construct called 'lambda' \0/

This lambda function is not same lambda FP languages.

'''

def sFastExp(b, e):
    if(e < 0):
        b = 1/b
        e = -e
    elif(e == 0):
        return 1.0
    elif(e == 0):
        return b
    rs = 1
    while(e > 0):
        if(e & 1 == 1):
            rs *= b
        #operador de divisao inteira
        #e //= 2
        e = e >> 1
        b *= b
    return rs

'''
    olha a funcao anonima ai
'''
fxlExp = lambda x,y: x**y
    
print("%f, %f\n"  % (fxlExp(15,-3), sFastExp(15,-3)))


'''
A declaracao lambda e tipicamente utilizada com conceitos
como filter(), map() e reudce()
'''

_list = range(1, 11, 1)
fx = lambda x : x % 4 == 0
print(filter(fx , _list))
print(map(fx, _list))

def cube(x):
    return x * x * x
'''
http://www.python-course.eu/python3_lambda.php
as funcoes passadas para reduce tem que ter 2 argumentos
#demorouparaentederoexception
'''
# exemplo de fatorial
_s = functools.reduce(lambda x,y: x*y, range(1,10))
print(_s)

# usando randomizacao

#print(random.randrange(0,1001,1))
_new_list = random.shuffle([1,2,3,4,5])
print(_new_list)

#exemplo de minimo numa lista
_new_list = random.sample(range(30), 5)
print(_new_list)
_s = functools.reduce(lambda x,y: x if x < y else y, _new_list)
print(_s)


if __name__ == '__main__':
    pass