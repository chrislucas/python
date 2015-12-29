'''
Created on Dec 21, 2015

@author: christoffer

'''
from __builtin__ import tuple
lista = ['A', 'B', 'C']
# Tuplas
# Semelhantes as lista, porem sao imutaveis:
# nao se pode alterar itens, apaga-los ou adicionar novos itens

# AS tuplas sao mais eficientes do que as listas convencionais, consomente
# menos recursos computacionais(memoria), por serem estruturaas mais simples
# igualmente sao as strings imutaveis em relacao as mutaveis

tupla = (1,[],2,3,4,10)     # os parentes sao opcionais

# TypeError: 'tuple' object does not support item assignment
# tupla[0] = 12

# uma lista pode ser convertida para uma tupla
tuplaA = tuple(lista)
# mesmo uma tupla formada por elementos mutaveis, nao pode
# ter seus elementos modificados
#tuplaA[1] = 'a'
#tuplaA += ['a']
#tuplaA[0].append('Z')
#tupla[0].append(6)
tupla[1].append(3)
tupla[1].append(56)

def addToTuple(tup, pos, e):
    tup = tup[:pos] + (e,) + tup[pos:]
    return tup

print tupla, (11,)
print addToTuple(tupla, 2, 100)

lista = list(tupla)

def printList(lista):
# lista vazia e avaliada como FALSE
    while lista :
        print lista.pop(), len(lista)

#printList(lista)
lista += ['Z', 'W', 'X', 'Y']
#printList(lista)

tuplaB = ([1,2], 4)
tuplaB[0].append(3)
tuplaB[0].append(lista)
print tuplaB
