'''
Created on Dec 21, 2015

@author: christoffer
'''

# Set: sequencias mutaveis univocas nao ordenadas
# FronzenSet: sequencias imutaveis univocas nao ordenadas

# range(start, stop, step)

setA = set(range(3))
setB = set(range(10,7,-1))
setC = set(range(2,10,2))

#print setC, range(2, 10, 2), set(range(10, -7, -2))
tA = (1,2,3)
tB = (1,-90)
#print set(tA).union(set(list(()))).union(tB)
'''
print set([10, 20, 30]).difference(set([10, 21, 30]))
print set([10, 20, 30]).difference([10, 21, 30])
print set([10, 20, 30]).intersection(set([10, 21, 30]))
'''
# verificar se um conjunto esta contido noutro
print set(range(1, 10)).issuperset([0, 1])
# testa se existe elementos em comum entre set1 e set2
print set(range(10, 2, -2)).isdisjoint([0,2,4])