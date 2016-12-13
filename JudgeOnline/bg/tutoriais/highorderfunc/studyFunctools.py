'''
Created on 21 de nov de 2016

@author: christoffer
'''

# https://docs.python.org/2/library/functools.html

from random import sample, shuffle

def run_randomic_array():
    # https://docs.python.org/3/library/random.html
    _nums = sample( list(range(0, 50)) , 3)
    print(*_nums)
    pass
#run_randomic_array()

def run_test_os_module():
    from os import environ
    for x in environ:
        print(x)
    print(environ['PYTHONPATH'])


def run_test_shuffle():    
    items = shuffle(range(0, 50))
    print(items)
run_test_shuffle()


if __name__ == '__main__':
    pass

'''
Modulo functools eh um modulo para funcoes higher-order
Em geral funcoes que retornam funcoes ou recebem-nas por parametro
'''

