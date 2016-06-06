'''
Created on 6 de jun de 2016

@author: C.Lucas

http://www.tutorbrasil.com.br/estudo_matematica_online/logaritmos/logaritmos_05_consequencias_definicao.php
http://www.tutorbrasil.com.br/estudo_matematica_online/logaritmos/logaritmos_08_mudanca_de_base.php

'''
from math import log, log10
from sys import stdout

def log(lg, base):
    return log10(lg) / log10(base)

stdout.write("%f" % (log(100, 1000)))

if __name__ == '__main__':
    pass