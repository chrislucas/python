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

print(getCurrentMilliseconds()())

if __name__ == '__main__':
    pass