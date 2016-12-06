'''
Created on 4 de dez de 2016

@author: C.Lucas
'''

'''
http://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
Exemplo de como usar o metodo time e pegar o tempo e milissegundos
de quebra fazer uns testes com keyword lambda
'''


'''
http://www.secnetix.de/olli/Python/lambda_functions.hawk
http://www.python-course.eu/python3_lambda.php
Lambda: Permite criar funcoes anonimas
'''
def getCurrentMilliseconds():
    from time import time
    tm = lambda : int(round(time() * 1000))
    # tm agora eh uma funcao
    return tm
#print(getCurrentMilliseconds()())

def getReader():
    from sys import stdin
    return lambda : stdin.readline().strip()
#print(getReader()())

'''
recurson interessante da funcao lambda em python
Na funcao definida abaixo, o parametro 'm' torna-se-a
um parametro default
A funcao abaixo retorna uma outra funcao criada em tempo
de execucao. O valor que dessa funcao varia conforme o valor
passado ao chama-la.
'''
def fx(m):
    return lambda x: [x, m] #x + m# print(x, m)
'''
fA = fx(15)
print(fA(10))
print(fA(-21))
fA = fx(31)
print(fA(11))
'''

'''
fx = lambda x,y : x**y
print(fx(12,3))
'''


if __name__ == '__main__':
    pass