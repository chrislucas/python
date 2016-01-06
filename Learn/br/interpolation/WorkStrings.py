'''
Created on 31 de dez de 2015

@author: C.Lucas
'''
import string, ctypes
# alfabeto
a = string.ascii_letters;
# print(a)

# deslocano o alfabeto uma letra para frente
b = a[1:] + a[0]
#print(b)

# a funcao maketrans cria um mapa (chave, valor)
# com as variaveis passadas por parametro
# relacionando-as
# http://stackoverflow.com/questions/10329290/python-3-x-using-string-maketrans-in-order-to-create-a-unicode-character-tran
mapTranslate = str.maketrans(a, b)
#print(mapTranslate)
print( 'Olha que coisa'.translate(mapTranslate) )


# Mutable Strings
#s = 'Hello World'
#mutable = ctypes.create_string_buffer(s, len(s))
#mutable[5:] = ''.join(reversed(mutable[5:]))
#print(mutable)

if __name__ == '__main__':
    pass