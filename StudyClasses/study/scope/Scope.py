'''
Created on 7 de jan de 2016

@author: C.Lucas
''' 

'''
variaveis globais pode ser ofuscadas por variaveis locais
'''
# varuavek global
variable = 3

def f(d):
    # varuavek local
    variable = d % 2
    return variable

#print(locals())
#print(globals())

'''
para evitar que uma variavel global seja ofuscada
por uma variavel local, use a keyword 'global'
'''

def sumList(lista):
    global summ
    for item in lista:
        if type(item) is list:
            sumList(item)
        else:
            summ += item
summ = 0
sumList([list(range(1,3)), list(range(3,6)), 6])
p = list(range(1,3))
print(p)
#sumList([[1,2], [3,4,5], 6])
print (summ)

# testando a funcao splt
print ('test function split'.split(sep=' '))


if __name__ == '__main__':
    pass