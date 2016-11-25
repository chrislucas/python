'''
Created on 22 de nov de 2016

@author: C.Lucas
'''

if __name__ == '__main__':
    pass

# https://docs.python.org/3/library/random.html#random.SystemRandom
# na versao 3.5 esse modulo nao funciona, ou pelo meos eu nao sei fazer funcionar

from random import choice, sample, random, getrandbits
from os import urandom
'''
Segundo a documentacao da biblioteca random.py no site official do
python, qyuse todas as funcoes do modulo dependen da funcao random
que gera numeros de ponto flutuante randomicos no intervalo (00., 1.0))

Pytyhon usa o como core para geracao de numeros pseudo randomicos Mersenne Twister

Pesquisar: Mersenne Twister
https://en.wikipedia.org/wiki/Mersenne_Twister
https://gist.github.com/banksean/300494

'''

def run_choice_method():
    print(choice("tesadasdasdas"))
    
#run_choice_method()

'''
Pesquisar por
Gaussian distribution
Log normal distribution
https://pt.wikipedia.org/wiki/Distribui%C3%A7%C3%A3o_log-normal

'''

def run_random():
    x = 0
    while x < len(list(range(60))):
        print(random())
        x  = x.__add__(1)

# run_random()

# https://docs.python.org/3/library/os.html#os.urandom
def run_os_random():
    x = 0
    while x < len(list(range(60))):
        print(urandom(3))
        x += 1

#run_os_random()

def run_getrandbit(n):
    '''
    retorna um interio com k random bits
    o que me faz crer que esse inteiro nao sera
    > 2 << k - 1
    '''
    print(getrandbits(n))   
#run_getrandbit(4)

def run_random_sample():
    print(*sample(list(range(60)), 3))
run_random_sample()
