'''
Created on Dec 21, 2015

@author: christoffer
'''
from __builtin__ import set

#Mapa, dicionario
# Uma lista de associacoes, composta por uma chave unica
# uma estrutura correspondente.
# dicionarios sao mutaveis tais como as listas
dicionario = {'a' : 10, 'b' : range(20, 2, -2)}
dicionario['a'] = range(1, 20, 2)

'''
for idx, e in enumerate(dicionario) :
    print idx, dicionario[e]
''' 
'''
for e in dicionario.items() :
    print e
'''

print dicionario.values()
print dicionario.keys()
print dicionario.items()

# [] lista
# () tupla
# {} dicionario


#for idx, n in enumerate(set([range()]))

if __name__ == '__main__':
    pass