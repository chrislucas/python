'''
Created on Dec 21, 2015

@author: christoffer

'''

lista = ['a','z', 'x', 'b', 'd']
from sys import stdout
'''
for char in lista:
    stdout.write(char)
'''
# a funcao enumerate(lst) retorna uma tupla
# de 2 elementos a cada iteracao: um numero sequencial e um elemento da lista
for idx, char in enumerate(lista):
    print idx, '=>', char


# trocando o ultimo elemento da lista
lista[-1] = 'e'
print lista, enumerate(lista)
# imprimindo subconjunto do array 'lista' n:m, m inclusive 
print lista[1:3]
